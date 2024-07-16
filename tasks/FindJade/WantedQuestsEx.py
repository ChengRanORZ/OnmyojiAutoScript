import importlib
from tasks.WantedQuests.config import WantedQuests, CooperationType


def need_invite_vip(self):
    return True


def get_invite_vip_name(self, ctype: CooperationType):
    if not self.fade_conf:
        return ""
    self.fade_conf.get_invite_name(ctype)

    if type == CooperationType.Jade:
        return "子曾经日"
    else:
        return "粘贴"
    pass


def next_run():
    pass


def invite_success_callback(self, ctype: CooperationType, name: str):
    if not self.fade_conf:
        return
    self.fade_conf.update_invite_history(ctype, name)

    pass
