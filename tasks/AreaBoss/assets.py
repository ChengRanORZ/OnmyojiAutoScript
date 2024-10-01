from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class AreaBossAssets: 


	# Click Rule Assets
	# 悬赏按钮 
	C_AB_REWARD_BTN = RuleClick(roi_front=(1190,100,50,120), roi_back=(1190,100,50,120), name="ab_reward_btn")
	# 热门按钮 
	C_AB_FAMOUS_BTN = RuleClick(roi_front=(1190,220,50,120), roi_back=(1190,220,50,120), name="ab_famous_btn")
	# 收藏按钮 
	C_AB_COLLECTION_BTN = RuleClick(roi_front=(1190,580,50,120), roi_back=(1190,580,50,120), name="ab_collection_btn")
	# 筛选中 除悬赏外 第一个boss的头像位置 
	C_AB_BOSS_PHOTO_1 = RuleClick(roi_front=(940,210,95,70), roi_back=(940,210,95,70), name="ab_boss_photo_1")
	# 筛选中 除悬赏外 第二个boss的头像位置 
	C_AB_BOSS_PHOTO_2 = RuleClick(roi_front=(940,365,95,70), roi_back=(940,365,95,70), name="ab_boss_photo_2")
	# 筛选中 除悬赏外 第三个boss的头像位置 
	C_AB_BOSS_PHOTO_3 = RuleClick(roi_front=(940,520,95,70), roi_back=(940,520,95,70), name="ab_boss_photo_3")
	# 筛选中 除悬赏外 滑动到最底部时 第一个boss的头像位置 即倒数第三个 
	C_AB_BOSS_PHOTO_MINUS_3 = RuleClick(roi_front=(940,255,95,70), roi_back=(940,255,95,70), name="ab_boss_photo_minus_3")
	# 筛选中 除悬赏外 滑动到最底部时 第二个boss的头像位置 即倒数第二个 
	C_AB_BOSS_PHOTO_MINUS_2 = RuleClick(roi_front=(940,410,95,70), roi_back=(940,410,95,70), name="ab_boss_photo_minus_2")
	# 筛选中 除悬赏外 滑动到最底部时 第三个boss的头像位置 即倒数第一个 
	C_AB_BOSS_PHOTO_MINUS_1 = RuleClick(roi_front=(940,560,95,70), roi_back=(940,560,95,70), name="ab_boss_photo_minus_1")
	# 筛选中 悬赏中 第一个boss的头像位置 
	C_AB_BOSS_REWARD_PHOTO_1 = RuleClick(roi_front=(940,250,95,70), roi_back=(940,250,95,70), name="ab_boss_reward_photo_1")
	# 筛选中 悬赏中 第二个boss的头像位置 
	C_AB_BOSS_REWARD_PHOTO_2 = RuleClick(roi_front=(940,375,95,70), roi_back=(940,375,95,70), name="ab_boss_reward_photo_2")
	# 筛选中 悬赏中 第三个boss的头像位置 
	C_AB_BOSS_REWARD_PHOTO_3 = RuleClick(roi_front=(940,500,95,70), roi_back=(940,500,95,70), name="ab_boss_reward_photo_3")
	# 筛选中 悬赏中 滑动到最底部时 第一个boss的头像位置 即倒数第三个 
	C_AB_BOSS_REWARD_PHOTO_MINUS_3 = RuleClick(roi_front=(940,335,95,70), roi_back=(940,335,95,70), name="ab_boss_reward_photo_minus_3")
	# 筛选中 悬赏中 滑动到最底部时 第二个boss的头像位置 即倒数第二个 
	C_AB_BOSS_REWARD_PHOTO_MINUS_2 = RuleClick(roi_front=(940,460,95,70), roi_back=(940,460,95,70), name="ab_boss_reward_photo_minus_2")
	# 筛选中 悬赏中 滑动到最底部时 第三个boss的头像位置 即倒数第一个 
	C_AB_BOSS_REWARD_PHOTO_MINUS_1 = RuleClick(roi_front=(940,585,95,70), roi_back=(940,585,95,70), name="ab_boss_reward_photo_minus_1")
	# 当前选择 的极地鬼层数 
	C_AB_JI_FLOOR_SELECTED = RuleClick(roi_front=(380,120,70,30), roi_back=(380,120,70,30), name="ab_ji_floor_selected")


	# Swipe Rule Assets
	# 筛选列表 手指向上滑动 
	S_AB_FILTER_UP = RuleSwipe(roi_front=(920,680,10,10), roi_back=(1130,230,10,10), mode="default", name="ab_filter_up")
	# 筛选列表 手指向下滑动 
	S_AB_FILTER_DOWN = RuleSwipe(roi_front=(1130,230,10,10), roi_back=(920,680,10,10), mode="default", name="ab_filter_down")
	# 极地鬼 层数列表 手指向下滑动  
	S_AB_FLOOR_DOWN = RuleSwipe(roi_front=(390,260,10,10), roi_back=(450,500,10,10), mode="default", name="ab_floor_down")
	# 普通地鬼 等级滑轨 手指向右滑动  
	S_AB_LEVEL_RIGHT = RuleSwipe(roi_front=(0,0,10,10), roi_back=(570,270,10,10), mode="default", name="ab_level_right")


	# Image Rule Assets
	# 探索图标 
	I_EXPLORE = RuleImage(roi_front=(758,122,66,77), roi_back=(339,104,836,120), threshold=0.8, method="Template matching", file="./tasks/AreaBoss/res/res_explore.png")
	# 地狱鬼王图标 
	I_AREA_BOSS = RuleImage(roi_front=(639,636,65,68), roi_back=(606,619,145,100), threshold=0.8, method="Template matching", file="./tasks/AreaBoss/res/res_area_boss.png")
	# 蓝色的返回 
	I_BACK_BLUE = RuleImage(roi_front=(51,30,51,52), roi_back=(4,1,128,110), threshold=0.8, method="Template matching", file="./tasks/AreaBoss/res/res_back_blue.png")
	# 右上边选中鬼王的 
	I_FILTER = RuleImage(roi_front=(1116,33,35,31), roi_back=(1076,19,98,78), threshold=0.8, method="Template matching", file="./tasks/AreaBoss/res/res_filter.png")
	# 除悬赏外 选中第一个鬼王的 
	I_BATTLE_1 = RuleImage(roi_front=(1066,210,100,100), roi_back=(1066,210,100,100), threshold=0.8, method="Template matching", file="./tasks/AreaBoss/res/res_battle_1.png")
	# 除悬赏外 选中第二个鬼王的 
	I_BATTLE_2 = RuleImage(roi_front=(1068,364,100,100), roi_back=(1068,364,100,100), threshold=0.8, method="Template matching", file="./tasks/AreaBoss/res/res_battle_2.png")
	# 除悬赏外 选中第三个鬼王的 
	I_BATTLE_3 = RuleImage(roi_front=(1071,521,100,100), roi_back=(1071,521,100,100), threshold=0.8, method="Template matching", file="./tasks/AreaBoss/res/res_battle_3.png")
	# 点击挑战 
	I_FIRE = RuleImage(roi_front=(1109,490,100,73), roi_back=(1075,463,150,158), threshold=0.8, method="Template matching", file="./tasks/AreaBoss/res/res_fire.png")
	# 跟buff冲突弃用 
	I_CLOSE_RED = RuleImage(roi_front=(1190,24,37,38), roi_back=(1190,24,37,38), threshold=0.8, method="Template matching", file="./tasks/AreaBoss/res/res_close_red.png")
	# 红色关闭 
	I_AB_CLOSE_RED = RuleImage(roi_front=(1194,24,38,37), roi_back=(1194,24,38,37), threshold=0.8, method="Template matching", file="./tasks/AreaBoss/res/res_ab_close_red.png")
	# 筛选中 选中悬赏标识 
	I_AB_FILTER_TITLE_REWARD = RuleImage(roi_front=(920,110,190,70), roi_back=(920,110,190,70), threshold=0.8, method="Template matching", file="./tasks/AreaBoss/res/ab_filter_title_reward.png")
	# 筛选中 选中热门标识 
	I_AB_FILTER_TITLE_FAMOUS = RuleImage(roi_front=(920,110,190,70), roi_back=(920,110,190,70), threshold=0.8, method="Template matching", file="./tasks/AreaBoss/res/ab_filter_title_famous.png")
	# 筛选中 选中收藏标识 
	I_AB_FILTER_TITLE_COLLECTION = RuleImage(roi_front=(920,110,190,70), roi_back=(920,110,190,70), threshold=0.8, method="Template matching", file="./tasks/AreaBoss/res/ab_filter_title_collection.png")
	# 筛选界面打开标识 
	I_AB_FILTER_OPENED = RuleImage(roi_front=(840,110,130,70), roi_back=(840,110,130,70), threshold=0.9, method="Template matching", file="./tasks/AreaBoss/res/ab_filter_opened.png")
	# 极地鬼标识 出现此图片表明 是 极地鬼 
	I_AB_DIFFICULTY_JI = RuleImage(roi_front=(260,100,70,70), roi_back=(260,100,70,70), threshold=0.8, method="Template matching", file="./tasks/AreaBoss/res/ab_difficulty_ji.png")
	# 极地鬼标识 出现此图片表明 是 普通地鬼 
	I_AB_DIFFICULTY_NORMAL = RuleImage(roi_front=(260,100,70,70), roi_back=(260,100,70,70), threshold=0.8, method="Template matching", file="./tasks/AreaBoss/res/ab_difficulty_normal.png")
	# 普通地鬼 更改等级 的把手 
	I_AB_LEVEL_HANDLE = RuleImage(roi_front=(170,250,400,75), roi_back=(170,250,400,75), threshold=0.8, method="Template matching", file="./tasks/AreaBoss/res/ab_level_handle.png")
	# 普通地鬼 等级为60 标志 
	I_AB_LEVEL_60 = RuleImage(roi_front=(300,160,110,100), roi_back=(300,160,110,100), threshold=0.8, method="Template matching", file="./tasks/AreaBoss/res/ab_level_60.png")
	# 极地鬼 层数列表打开 标志 
	I_AB_JI_FLOOR_LIST_CHECK = RuleImage(roi_front=(390,150,60,290), roi_back=(390,150,60,290), threshold=0.8, method="Template matching", file="./tasks/AreaBoss/res/ab_ji_floor_list_check.png")
	# 极地鬼 一层 
	I_AB_JI_FLOOR_ONE = RuleImage(roi_front=(390,150,60,290), roi_back=(390,150,60,290), threshold=0.8, method="Template matching", file="./tasks/AreaBoss/res/ab_ji_floor_one.png")
	# 小组内未取得名次 
	I_AB_GROUP_RANK_NONE = RuleImage(roi_front=(890,415,95,85), roi_back=(890,415,95,85), threshold=0.8, method="Template matching", file="./tasks/AreaBoss/res/ab_rank_none.png")


	# Ocr Rule Assets
	# 击杀最多 
	O_AB_KILL_BEST = RuleOcr(roi=(942,123,157,52), area=(942,123,157,52), mode="Single", method="Default", keyword="击杀最多", name="ab_kill_best")
	# 我的收藏 
	O_AB_MY_COLLECT = RuleOcr(roi=(949,124,129,53), area=(949,124,129,53), mode="Single", method="Default", keyword="我的收藏", name="ab_my_collect")
	# 热门 
	O_AB_FAMOUS = RuleOcr(roi=(1190,220,50,120), area=(1190,220,50,120), mode="Single", method="Default", keyword="热门", name="ab_famous")
	# 收藏 
	O_AB_COLLECTING = RuleOcr(roi=(1190,580,50,120), area=(1190,580,50,120), mode="Single", method="Default", keyword="收藏", name="ab_collecting")
	# 挑战人数 
	O_AB_NUM_OF_CHALLENGE = RuleOcr(roi=(270,630,150,36), area=(270,630,150,36), mode="Digit", method="Default", keyword="", name="ab_num_of_challenge")


