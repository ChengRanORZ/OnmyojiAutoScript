import importlib
from tasks.WantedQuests.config import WantedQuests, CooperationType


def need_invite_vip(self):
    return True


def get_invite_vip_name(self, ctype: CooperationType):
    if not self.fade_conf:
        return ""
    return self.fade_conf.get_invite_name(ctype)


def next_run(self):
    pass


def invite_success_callback(self, ctype: CooperationType, name: str):
    if not self.fade_conf:
        return
    self.fade_conf.update_invite_history(ctype, name)

    pass
