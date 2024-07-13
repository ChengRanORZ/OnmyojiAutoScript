from datetime import datetime
from pydantic import Field, BaseModel
from tasks.Component.config_base import ConfigBase
from tasks.Component.config_scheduler import Scheduler
from typing import List


class AccountInfo(BaseModel):
    # def __init__(self, character: str, svr: str, account: str = None, appleOrAndroid: bool = True):
    #     self.character = character
    #     self.svr = svr
    #     self.account = account
    #     self.appleOrAndroid = appleOrAndroid

    character: str = Field(default="", description='character_help')
    svr: str = Field(default="", description="svr_help")
    account: str = Field(default="", description="account_help")
    appleOrAndroid: bool = Field(default=True, description="apple_or_android_help")
    # 上一次执行成功的时间 ,防止出错时重复登录浪费时间
    last_complete_time: datetime = Field(default=datetime(1970, 1, 1, 1, 1, 1), description="last_complete_time_help")


defaultAccountInfo = AccountInfo()
defaultAccountInfo.account = "dAccount"
defaultAccountInfo.svr = "dSvr"
defaultAccountInfo.character = "dCharacter"
defaultAccountInfo.appleOrAndroid = True
defaultAccountInfo.last_complete_time = datetime(1970, 1, 1, 1, 1, 1)


class FindJadeConfig(BaseModel):
    find_jade_accounts_info: List[AccountInfo] = Field(default=[defaultAccountInfo],
                                                       description='find_jade_accounts_info_help')


class FindJade(ConfigBase):
    scheduler: Scheduler = Field(default_factory=Scheduler)
    find_jade_config: FindJadeConfig = Field(default_factory=FindJadeConfig)
