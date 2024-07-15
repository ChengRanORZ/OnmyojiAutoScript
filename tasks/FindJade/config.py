from datetime import datetime
from pydantic import Field, BaseModel
from tasks.Component.SwitchAccount.switch_account_config import AccountInfo
from tasks.Component.config_base import ConfigBase
from tasks.Component.config_scheduler import Scheduler
from module.config.utils import write_file

defaultAccountInfo = AccountInfo()
defaultAccountInfo.account = "dAccount"
defaultAccountInfo.accountAlias = 'dAcc0unt#dAccOunt'
defaultAccountInfo.svr = "dSvr"
defaultAccountInfo.character = "dCharacter"
defaultAccountInfo.appleOrAndroid = True
defaultAccountInfo.last_complete_time = datetime(1970, 1, 1, 1, 1, 1)


class FindJade(ConfigBase):
    scheduler: Scheduler = Field(default_factory=Scheduler)
    find_jade_json_path: str = Field(default="./config/findjade/find_jade.json", description="json conf file path")


class FindJadeJSON(BaseModel):
    jade_to_list: str
    find_jade_accounts_info: list[AccountInfo]

    def save2file(self, conf_path):
        write_file(conf_path, self.dict())
