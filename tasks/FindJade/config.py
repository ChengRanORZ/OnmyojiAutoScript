from datetime import datetime, timedelta
from pydantic import Field, BaseModel
from tasks.Component.SwitchAccount.switch_account_config import AccountInfo
from tasks.Component.config_base import ConfigBase
from tasks.Component.config_scheduler import Scheduler
from module.config.utils import write_file
from tasks.WantedQuests.config import CooperationSelectMaskDescription, CooperationSelectMask, CooperationType


class FindJadeConfig(BaseModel):
    find_jade_json_path: str = Field(default='./config/findjade/find_jade.json', description='json conf file path')
    # extra: str = Field(default='')


class FindJade(ConfigBase):
    scheduler: Scheduler = Field(default_factory=Scheduler)
    find_jade_config: FindJadeConfig = Field(default_factory=FindJadeConfig)


class InviteInfo(BaseModel):
    # 被邀请人员昵称
    name: str = "defaultName"
    default_invite_type: CooperationSelectMaskDescription
    # 协作任务类型   上次邀请时间
    invited_types: dict

    def need_invite(self, ctype: CooperationType):
        if not ctype & CooperationSelectMask[self.default_invite_type.value]:
            return False
        # 判断是否邀请过
        if ctype not in self.invited_types:
            self.invited_types.setdefault(ctype, datetime(1970, 1, 1))
            return True
        lastTime = self.invited_types.get(ctype, default=datetime(1970, 1, 1))
        now = datetime.now()
        if now - lastTime > timedelta(hours=13):
            return True
        if (lastTime.hour >= 18 or lastTime.hour < 5) and (18 > now.hour >= 5):
            return True
        if (5 <= lastTime.hour < 18) and now.hour >= 18:
            return True
        return False


class FindJadeJSON(BaseModel):
    find_jade_accounts_info: list[AccountInfo]
    invite_info_list: list[InviteInfo]

    def get_invite_name(self, ctype: CooperationType):
        for info in self.invite_info_list:
            if info.need_invite(ctype):
                return info.name
        return ""

    def update_invite_history(self, ctype: CooperationType, name: str):
        # 更新邀请信息
        for info in self.invite_info_list:
            if info.name != name:
                continue
            info.invited_types.setdefault(ctype, datetime.now())

    def update_account_login_history(self, account: AccountInfo):
        accountInfoList = self.find_jade_accounts_info
        for info in accountInfoList:
            if info.character != account.character or info.svr != account.svr:
                continue
            info.last_complete_time = datetime.now()

    def save2file(self, conf_path):
        write_file(conf_path, self.dict())
