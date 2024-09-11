from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class GeneralBattleAssets: 


	# Click Rule Assets
	# description 
	C_WIN_1 = RuleClick(roi_front=(175,102,1054,99), roi_back=(175,102,1054,99), name="win_1")
	# description 
	C_WIN_2 = RuleClick(roi_front=(22,112,210,496), roi_back=(22,112,210,496), name="win_2")
	# description 
	C_WIN_3 = RuleClick(roi_front=(1059,114,206,468), roi_back=(1059,114,206,468), name="win_3")
	# description 
	C_REWARD_1 = RuleClick(roi_front=(606,603,325,87), roi_back=(606,603,325,87), name="reward_1")
	# description 
	C_REWARD_2 = RuleClick(roi_front=(25,134,224,472), roi_back=(25,134,224,472), name="reward_2")
	# description 
	C_REWARD_3 = RuleClick(roi_front=(1092,156,168,437), roi_back=(1092,156,168,437), name="reward_3")


	# Click Rule Assets
	# 预设队伍1 
	C_PRESET_TEAM_1 = RuleClick(roi_front=(196,234,464,114), roi_back=(196,234,464,114), name="preset_team_1")
	# 预设队伍2 
	C_PRESET_TEAM_2 = RuleClick(roi_front=(197,358,465,103), roi_back=(197,358,465,103), name="preset_team_2")
	# 预设队伍3 
	C_PRESET_TEAM_3 = RuleClick(roi_front=(195,480,462,100), roi_back=(195,480,462,100), name="preset_team_3")
	# 预设队伍4 
	C_PRESET_TEAM_4 = RuleClick(roi_front=(193,596,464,35), roi_back=(193,596,464,35), name="preset_team_4")
	# 预设组1 
	C_PRESET_GROUP_1 = RuleClick(roi_front=(28,238,134,56), roi_back=(28,238,134,56), name="preset_group_1")
	# 预设组2 
	C_PRESET_GROUP_2 = RuleClick(roi_front=(31,298,132,60), roi_back=(31,298,132,60), name="preset_group_2")
	# 预设组3 
	C_PRESET_GROUP_3 = RuleClick(roi_front=(31,362,135,59), roi_back=(31,362,135,59), name="preset_group_3")
	# 预设组4 
	C_PRESET_GROUP_4 = RuleClick(roi_front=(29,427,133,57), roi_back=(29,427,133,57), name="preset_group_4")
	# 预设组5 
	C_PRESET_GROUP_5 = RuleClick(roi_front=(31,489,133,60), roi_back=(31,489,133,60), name="preset_group_5")
	# 预设组6 
	C_PRESET_GROUP_6 = RuleClick(roi_front=(31,549,132,63), roi_back=(31,549,132,63), name="preset_group_6")
	# 预设组7 
	C_PRESET_GROUP_7 = RuleClick(roi_front=(29,615,137,63), roi_back=(29,615,137,63), name="preset_group_7")
	# 从左开始第一个绿标 
	C_GREEN_LEFT_1 = RuleClick(roi_front=(128,433,90,150), roi_back=(128,433,90,150), name="green_left_1")
	# 从左开始第二个绿标 
	C_GREEN_LEFT_2 = RuleClick(roi_front=(371,385,81,145), roi_back=(371,385,81,145), name="green_left_2")
	# 从左开始第三个绿标 
	C_GREEN_LEFT_3 = RuleClick(roi_front=(586,328,100,76), roi_back=(586,328,100,76), name="green_left_3")
	# 从左开始第四个绿标 
	C_GREEN_LEFT_4 = RuleClick(roi_front=(817,379,77,133), roi_back=(817,379,77,133), name="green_left_4")
	# 从左开始第五个绿标 
	C_GREEN_LEFT_5 = RuleClick(roi_front=(1059,416,85,145), roi_back=(1059,416,85,145), name="green_left_5")
	# 绿标阴阳师 
	C_GREEN_MAIN = RuleClick(roi_front=(590,454,88,178), roi_back=(590,454,88,178), name="green_main")
	# 战斗的时候有一定的概率随机点击 
	C_RANDOM_CLICK = RuleClick(roi_front=(104,79,1050,507), roi_back=(255,65,100,100), name="random_click")


	# Image Rule Assets
	# 奖励，就是那个魂 
	I_REWARD = RuleImage(roi_front=(547,518,172,96), roi_back=(547,518,172,96), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_reward.png")
	# 预设的小图标 
	I_PRESET = RuleImage(roi_front=(30,640,60,180), roi_back=(30,640,60,180), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_preset.png")
	# 准备 
	I_PREPARE_HIGHLIGHT = RuleImage(roi_front=(1128,536,100,100), roi_back=(1128,536,100,100), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_prepare_highlight.png")
	# 战斗胜利 
	I_WIN = RuleImage(roi_front=(385,47,100,100), roi_back=(296,33,414,224), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_win.png")
	# 准备但是界面还未加载这个时候是黑色的 
	I_PREPARE_DARK = RuleImage(roi_front=(1131,538,100,100), roi_back=(1131,538,100,100), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_prepare_dark.png")
	# 失败 
	I_FALSE = RuleImage(roi_front=(413,124,100,100), roi_back=(413,124,100,100), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_false.png")
	# 确认预设的队伍 
	I_PRESET_ENSURE = RuleImage(roi_front=(352,643,141,50), roi_back=(305,625,236,83), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_preset_ensure.png")
	# 选择buff 
	I_BUFF = RuleImage(roi_front=(115,657,42,50), roi_back=(106,641,67,77), threshold=0.7, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_buff.png")
	# 觉醒加成 
	I_BUFF_AWAKEN = RuleImage(roi_front=(373,126,383,53), roi_back=(373,126,383,53), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_buff_awaken.png")
	# 御魂加成 
	I_BUFF_SOUL = RuleImage(roi_front=(377,192,371,56), roi_back=(377,192,371,56), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_buff_soul.png")
	# 金币加成50 
	I_BUFF_GOLD_50 = RuleImage(roi_front=(375,259,373,56), roi_back=(375,259,373,56), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_buff_gold_50.png")
	# 金币加成100 
	I_BUFF_GOLD_100 = RuleImage(roi_front=(371,329,389,54), roi_back=(371,329,389,54), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_buff_gold_100.png")
	# 经验加成50 
	I_BUFF_EXP_50 = RuleImage(roi_front=(378,400,370,50), roi_back=(378,400,370,50), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_buff_exp_50.png")
	# 经验加成100 
	I_BUFF_EXP_100 = RuleImage(roi_front=(372,463,386,50), roi_back=(372,463,386,50), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_buff_exp_100.png")
	# 左下角的位置指针 
	I_LOCAL = RuleImage(roi_front=(25,563,30,34), roi_back=(25,563,30,34), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_local.png")
	# description 
	I_STATISTICS = RuleImage(roi_front=(61,644,33,28), roi_back=(61,644,33,28), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_statistics.png")
	# 左上角的退出 
	I_EXIT = RuleImage(roi_front=(14,12,43,41), roi_back=(14,12,43,41), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_exit.png")
	# 退出确认 
	I_EXIT_ENSURE = RuleImage(roi_front=(674,388,135,63), roi_back=(674,388,135,63), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_exit_ensure.png")
	# 左上角好友图标 
	I_FRIENDS = RuleImage(roi_front=(89,14,36,36), roi_back=(89,14,36,36), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_friends.png")
	# 结算时左下角统计图标 
	I_REWARD_STATISTICS = RuleImage(roi_front=(51,629,54,59), roi_back=(51,629,54,59), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_reward_statistics.png")
	# 结算金币 
	I_REWARD_GOLD = RuleImage(roi_front=(943,312,97,69), roi_back=(943,312,97,69), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_reward_gold.png")
	# 针对封魔的特殊 
	I_DE_WIN = RuleImage(roi_front=(472,49,100,100), roi_back=(239,36,399,133), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_de_win.png")
	# description 
	I_PRESENT_LESS_THAN_5 = RuleImage(roi_front=(222,648,418,43), roi_back=(222,648,418,43), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_present_less_than_5.png")
	# 封魔的金币 
	I_DE_GOLD = RuleImage(roi_front=(61,52,30,25), roi_back=(45,33,65,64), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_de_gold.png")


	# Image Rule Assets
	# description 
	I_GREED_GHOST = RuleImage(roi_front=(56,40,45,45), roi_back=(56,40,45,45), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_greed_ghost.png")


	# Ocr Rule Assets
	# 准备 
	O_BATTLE_PREPARE = RuleOcr(roi=(1122,546,92,51), area=(1122,546,92,51), mode="Single", method="Default", keyword="准备", name="battle_prepare")


	# Swipe Rule Assets
	# description 
	S_BATTLE_RANDOM_LEFT = RuleSwipe(roi_front=(122,155,480,426), roi_back=(667,147,461,427), mode="default", name="battle_random_left")
	# description 
	S_BATTLE_RANDOM_RIGHT = RuleSwipe(roi_front=(719,138,417,392), roi_back=(237,163,387,394), mode="default", name="battle_random_right")


