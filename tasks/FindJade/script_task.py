import sys

import importlib
from datetime import datetime, timedelta
from dev_tools.assets_test import detect_image
from module.base.utils import load_module
from module.config.config import Config
from module.config.utils import read_file
from module.device.device import Device
from module.exception import TaskEnd
from pathlib import Path
from tasks.Component.SwitchAccount.switch_account import SwitchAccount
from tasks.FindJade import WantedQuestsEx
from tasks.FindJade.assets import FindJadeAssets
from tasks.FindJade.config import AccountInfo, FindJadeJSON
from tasks.GameUi.game_ui import GameUi
from tasks.GameUi.page import page_main
from tasks.WantedQuests.config import CooperationSelectMaskDescription, CooperationType
from tasks.base_task import BaseTask
from typing import List
from module.logger import logger


class ScriptTask(GameUi, FindJadeAssets):
    fade_conf: FindJadeJSON = None

    def run(self):
        self.ui_get_current_page()

        self.fade_conf = self.parse()
        for accountInfo in self.fade_conf.find_jade_accounts_info:
            self.custom_config(self.config)
            logger.info("start %s-%s ", accountInfo.character, accountInfo.svr)
            if not self.needLogin(accountInfo):
                logger.warning("%s Skipped last Login Time:%s", accountInfo.character, accountInfo.last_complete_time)
                continue
            suc = SwitchAccount(self.config, self.device, accountInfo).switchAccount()
            if not suc:
                continue
            #
            wq = self.CreatObjectFromModule("WantedQuests", config=self.config, device=self.device)
            wq.fade_conf = self.fade_conf

            try:
                wq.run()
            except TaskEnd as e:
                logger.warning("%s-%s TaskEnd", accountInfo.character, accountInfo.svr)
                # 更新配置文件中的时间
                self.fade_conf.update_account_login_history(accountInfo)
                self.fade_conf.save2file(self.config.find_jade.find_jade_config.find_jade_json_path)
                continue

        pass

    def custom_config(self, conf):
        conf.wanted_quests.wanted_quests_config.cooperation_only = True
        conf.wanted_quests.wanted_quests_config.cooperation_type = CooperationSelectMaskDescription.JadeAndFood
        conf.wanted_quests.wanted_quests_config.invite_friend_name = "却把烟花嗅"

    def parse(self) -> FindJadeJSON:
        """
            如果后期更改配置文件格式而做的先手准备,
        @return:
        @rtype:
        """
        conf_path = self.config.find_jade.find_jade_config.find_jade_json_path
        jsonData = read_file(conf_path)
        fjconf = FindJadeJSON(**jsonData)
        return fjconf

        # return [('缘神一世', '立秋', '150****2279', True),
        #         ('缘神二世', '立秋', 'luorq05332@163.com', True),
        #         ('停摆六世', '立秋', 'luorq05336@163.com', True),
        #         ('缘神一世', '立秋', '150****2279', True),
        #         ]

    def needLogin(self, item: AccountInfo):
        """
            根据上次登陆时间 判断是否需要登录查找
        @param item:
        @type item:
        """
        lastTime = item.last_complete_time
        now = datetime.now()
        if now - lastTime > timedelta(hours=13):
            return True
        if (lastTime.hour >= 18 or lastTime.hour < 5) and (18 > now.hour >= 5):
            return True
        if (5 <= lastTime.hour < 18) and now.hour >= 18:
            return True
        return False

    def CreatObjectFromModule(self, task_name: str, **kwargs):
        module_name = 'script_task'
        from pathlib import Path
        module_path = str(Path.cwd() / 'tasks' / task_name / (module_name + '.py'))

        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        WQEX = type("WQEX", (module.ScriptTask,), {
            "need_invite_vip": WantedQuestsEx.need_invite_vip,
            "get_invite_vip_name": WantedQuestsEx.get_invite_vip_name,
            "next_run": WantedQuestsEx.next_run,
            "invite_success_callback": WantedQuestsEx.invite_success_callback
        })
        wq = WQEX(**kwargs)
        return wq

    def save_jade_json(self):
        conf_path = self.config.find_jade.find_jade_config.find_jade_json_path
        self.fade_conf.save2file(conf_path)


if __name__ == '__main__':
    from module.config.config import Config
    from module.device.device import Device

    c = Config('oas1')
    d = Device(c)
    t = ScriptTask(c, d)
    # wq = t.CreatObjectFromModule("WantedQuests", config=t.config, device=t.device)
    # wq.need_invite_vip = WantedQuestsEx.need_invite_vip
    # wq.get_invite_vip_name = WantedQuestsEx.get_invite_vip_name
    # t.fade_conf = t.parse()
    #
    # t.fade_conf.update_invite_history(CooperationType.Jade, "却把烟花嗅")
    # t.fade_conf.save2file(".\\config\\findjade\\findjade.json")

    # print(wq.need_invite_vip())
    # t.fade_conf = t.parse()
    # t.fade_conf.save2file("F:/download/1.json")
    t.run()
