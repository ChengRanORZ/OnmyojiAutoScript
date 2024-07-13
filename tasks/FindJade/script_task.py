import sys

import importlib
from datetime import datetime,timedelta
from dev_tools.assets_test import detect_image
from module.base.utils import load_module
from module.config.config import Config
from module.device.device import Device
from module.exception import TaskEnd
from pathlib import Path
from tasks.Component.SwitchAccount.switch_account import SwitchAccount
from tasks.FindJade.assets import FindJadeAssets
from tasks.GameUi.game_ui import GameUi
from tasks.GameUi.page import page_main
from tasks.base_task import BaseTask
from typing import List
from module.logger import logger


class ScriptTask(GameUi, FindJadeAssets):
    def run(self):
        con = self.config
        self.ui_get_current_page()
        for item in self.parse():
            logger.info("start %s-%s ",item[0],item[1])
            if not self.needLogin(item):
                logger.warning("%s Skipped last Login Time:%s", item[0], item[4])
                continue
            suc = SwitchAccount(self.config, self.device, item[0], item[1], item[2], item[3]).switchAccount()
            if not suc:
                continue
            method = self.WantedQuestScript()
            try:
                method()
            except TaskEnd as e:
                logger.warning("%s-%s TaskEnd", item[0], item[1])
                # 更新配置文件中的时间
                accountInfoList = self.config.find_jade.find_jade_config.find_jade_accounts_info
                index = [item.character for item in accountInfoList].index(item[0])
                accountInfoList[index].last_complete_time = datetime.now()
                self.config.save()
                continue

        pass

    def parse(self) -> List[tuple]:
        """
            如果后期更改配置文件格式而做的先手准备,
        @return:
        @rtype:
        """
        confList = self.config.find_jade.find_jade_config.find_jade_accounts_info
        if not confList:
            return []
        retList = []
        for item in confList:
            retList.append((item.character, item.svr, item.account, item.appleOrAndroid, item.last_complete_time))
        return retList

        # return [('缘神一世', '立秋', '150****2279', True),
        #         ('缘神二世', '立秋', 'luorq05332@163.com', True),
        #         ('停摆六世', '立秋', 'luorq05336@163.com', True),
        #         ('缘神一世', '立秋', '150****2279', True),
        #         ]

    def needLogin(self, item: tuple):
        """
            根据上次登陆时间 判断是否需要登录查找
        @param item:
        @type item:
        """
        lastTime = item[4]
        now = datetime.now()
        if now - lastTime > timedelta(hours=13):
            return True
        if (lastTime.hour >= 18 or lastTime.hour < 5) and (18>now.hour >= 5):
            return True
        if (5 <= lastTime.hour < 18) and now.hour >= 18:
            return True
        return False

    def WantedQuestScript(self):
        module_name = 'script_task'
        module_path = str(Path.cwd() / 'tasks' / 'WantedQuests' / (module_name + '.py'))
        logger.info(f'module_path: {module_path}, module_name: {module_name}')
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        return module.ScriptTask(config=self.config, device=self.device).run


if __name__ == '__main__':
    from module.config.config import Config
    from module.device.device import Device

    c = Config('oas1')
    d = Device(c)
    t = ScriptTask(c, d)
    # t.parse()
    t.run()
