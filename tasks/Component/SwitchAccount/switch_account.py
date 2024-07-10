from module.config.config import Config
from module.device.device import Device
from tasks.Component.SwitchAccount.assets import SwitchAccountAssets
from tasks.Component.SwitchAccount.exit_game import ExitGame
from tasks.Component.SwitchAccount.login_account import LoginAccount
from tasks.GameUi.game_ui import GameUi
from tasks.GameUi.page import page_main, page_login
from tasks.base_task import BaseTask
from tasks.Restart.login import LoginHandler

from module.logger import logger


class SwitchAccount(LoginAccount, ExitGame, GameUi, SwitchAccountAssets):

    def __init__(self, config: Config, device: Device,
                 toCharacter: str, toSvr: str = None, toAccount: str = None, fromAppleOrAndroid=True,
                 fromAccount=None, fromSvr: str = None, fromCharacter: str = None, toAppleOrAndroid=True):
        super().__init__(config, device)
        self.fromCharacter = fromCharacter
        self.fromSvr = fromSvr
        self.fromAccount = fromAccount
        self.fromAppleOrAndroid = fromAppleOrAndroid
        self.toAccount = toAccount
        self.toSvr = toSvr
        self.toCharacter = toCharacter
        self.toAppleOrAndroid = toAppleOrAndroid

    def switchAccount(self):
        logger.info("start switchAccount %s-%s", self.toCharacter, self.toSvr)
        # 判断所处界面
        curPage = self.ui_get_current_page()

        if curPage != page_login and curPage != page_main:
            self.ui_goto(page_main)
        if curPage == page_main:
            self.exitGame()

        # 处于登录界面
        if not self.login(self.toCharacter, self.toSvr, self.toAccount, self.toAppleOrAndroid):
            return False
        logger.info("%s login suc", self.toCharacter)
        # 处理位于登录界面各种奇葩弹窗
        LoginHandler(self.config, self.device).app_handle_login()

        return True
