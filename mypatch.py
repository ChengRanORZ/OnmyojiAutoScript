import sys

import importlib
from module.atom.click import RuleClick
from module.atom.gif import RuleGif
from module.atom.image import RuleImage
from module.atom.long_click import RuleLongClick
from module.atom.ocr import RuleOcr
from typing import Union
import tasks


def appear_then_click_CRORZ(self,
                            target: RuleImage | RuleGif,
                            action: Union[RuleClick, RuleLongClick] = None,
                            interval: float = None,
                            threshold: float = None,
                            duration: float = None):
    """
    出现了就点击，默认点击图片的位置，如果添加了click参数，就点击click的位置
    :param duration: 如果是长按，可以手动指定duration，不指定默认.单位是ms！！！！
    :param action: 可以是RuleClick, 也可以是RuleLongClick
    :param target: 可以是RuleImage后续支持RuleOcr
    :param interval:
    :param threshold:
    :return: True or False
    """
    if not (isinstance(target, RuleImage) or isinstance(target, RuleGif)):
        return False

    appear = self.appear(target, threshold=threshold)
    if not appear:
        return False
    # 界面有控件
    if not bool(interval):
        self.click(click=action if action else target)
        return appear
        # 有时间间隔限制
    # 强制增大interval
    if interval < 3:
        interval = 3

    is_clicked = self.click(click=action if action else target, interval=interval)
    return appear and is_clicked


def ui_click_CRORZ(self, click, stop, interval=1):
    """
    循环的一个操作，直到出现stop
    :param click:
    :param stop:
    :parm interval
    :return:
    """
    # 强制增大interval
    interval = 3 if interval < 3 else interval
    while 1:
        self.screenshot()
        if self.appear(stop):
            return True
        if isinstance(click, RuleImage) or isinstance(click, RuleGif):
            self.appear_then_click(click, interval=interval)
            continue
        if isinstance(click, RuleClick) and self.click(click, interval=interval):
            continue
        elif isinstance(click, RuleOcr) and self.ocr_appear_click(click, interval=interval):
            continue


class SimplePatch():
    # modulePath-类名-方法名-patch方法名
    patch_method_list: list[tuple[str, str, str, str]] = [
        ('tasks', 'base_task.BaseTask', 'appear_then_click', 'appear_then_click_CRORZ'),
        ('tasks', 'base_task.BaseTask', 'ui_click', 'ui_click_CRORZ'),
    ]

    @classmethod
    def patch(cls):
        for item in SimplePatch.patch_method_list:
            SimplePatch.patch_one(item)

    @classmethod
    def patch_one(cls, item: tuple):
        # packageName  类名   原方法名    patch方法名
        # item = ('tasks', 'base_task.BaseTask', 'appear_then_click', 'appear_then_click_CRORZ')

        package_name, cls_path, method_name_origin, method_name_patch = item
        method_name_origin_bak = method_name_origin + "_bak"
        importlib.import_module('.base_task', package_name)
        cls_name = ""
        cls_obj = sys.modules[package_name]
        for n in cls_path.split('.'):
            cls_obj = getattr(cls_obj, n)
            cls_name = n
        if getattr(cls_obj, cls_name + "_origin", None) is None:
            setattr(cls_obj, method_name_origin_bak, getattr(cls_obj, method_name_origin))
            setattr(cls_obj, method_name_origin, globals()[method_name_patch])
            setattr(cls_obj, "patched", True)
        pass
