from datetime import datetime
from pydantic import Field, BaseModel
from tasks.Component.SwitchAccount.switch_account_config import AccountInfo
from tasks.Component.config_base import ConfigBase
from tasks.Component.config_scheduler import Scheduler
from typing import List

defaultAccountInfo = AccountInfo()
defaultAccountInfo.account = "dAccount"
defaultAccountInfo.accountAlias = 'dAcc0unt#dAccOunt'
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
