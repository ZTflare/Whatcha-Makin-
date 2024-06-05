import pygame, random
from sys import exit



screen = pygame.display.set_mode((1000,1000))
ChoppedBeefAmount = 0

Time = 500
Score = 0
FoodMade = 0
OverTime = 0
FoodWasted = 0
FinalScore = 0

player_index = 0
player2_index = 0
StoveAnimation = 0
Stove2Animation = 0
fryer1Animation = 0
BurgerTime = 30
Stove1Timer = 0
Stove2Timer = 0
fryer1Timer = 0
player1inv_buffer = 0
player2inv_buffer = 0
player1_inv2 = 'None'
player1_inv = 'None'
player2_inv2 = 'None'
player2_inv = 'None'
player1inv_subparty = 'None'
player2inv_subparty = 'None'
P1inv2ID = 0
P2inv2ID = 0
stove1Slot = 'None'
stove2Slot = 'None'
fryer1Slot = 'None'
P1invID = 0
P2invID = 0
StoveTimerStage = 0
fryerTimerStage = 0
BMS_Stand = []
npctag = []
NPC1_index = 0
NPC2_index = 0
NPC3_index = 0
NPC4_index = 0
NPC5_index = 0

beeftablestate = 0
NPCMoveTime = 0
NPC2MoveTime = 0
NPC1_order = 0
NPC2_order = 0
NPC1_order_buffer = 0
NPC2_order_buffer = 0
#-----------------------# 
NPC3MoveTime = 0
NPC4MoveTime = 0
NPC5MoveTime = 0
NPC3_order = 0
NPC4_order = 0
NPC5_order = 0
NPC3_order_buffer = 0
NPC4_order_buffer = 0
NPC5_order_buffer = 0


def player_animation():
    global Player1walk, player_index, Player1_surf, Player2walk, player2_index, Player2_surf

    if down=="Y":
        player_index += 0.1
        if player_index >= 2:
            player_index = 0
        Player1_surf = Player1walk[int(player_index)]
        Player1_surf = pygame.transform.scale(Player1_surf, PlayerImgSize)
    elif right=="Y":
        player_index += 0.1
        if player_index < 2:
            player_index = 3
        if player_index >= 4:
            player_index = 2
        Player1_surf = Player1walk[int(player_index)]
        Player1_surf = pygame.transform.scale(Player1_surf, PlayerImgSize)
    elif left=="Y":
        player_index += 0.1
        if player_index < 2:
            player_index = 3
        if player_index >= 4:
            player_index = 2
        Player1_surf = Player1walk[int(player_index)]
        Player1_surf = pygame.transform.scale(Player1_surf, PlayerImgSize)
        Player1_surf = pygame.transform.flip(Player1_surf, 180, 0)
    elif up=="Y":
        player_index += 0.1
        if player_index < 4:
            player_index = 5
        if player_index >= 6:
            player_index = 4
        Player1_surf = Player1walk[int(player_index)]
        Player1_surf = pygame.transform.scale(Player1_surf, PlayerImgSize)
    else:
        player_index += 0.1
        if player_index < 6:
            player_index = 6
        if player_index >= 9:
            player_index = 6
        Player1_surf = Player1walk[int(player_index)]
        Player1_surf = pygame.transform.scale(Player1_surf, PlayerImgSize)
    
    if down2=="Y":
        player2_index += 0.1
        if player2_index >= 2:
            player2_index = 0
        Player2_surf = Player2walk[int(player2_index)]
        Player2_surf = pygame.transform.scale(Player2_surf, PlayerImgSize)
    elif right2=="Y":
        player2_index += 0.1
        if player2_index < 2:
            player2_index = 3
        if player2_index >= 4:
            player2_index = 2
        Player2_surf = Player2walk[int(player2_index)]
        Player2_surf = pygame.transform.scale(Player2_surf, PlayerImgSize)
    elif left2=="Y":
        player2_index += 0.1
        if player2_index < 2:
            player2_index = 3
        if player2_index >= 4:
            player2_index = 2
        Player2_surf = Player2walk[int(player2_index)]
        Player2_surf = pygame.transform.scale(Player2_surf, PlayerImgSize)
        Player2_surf = pygame.transform.flip(Player2_surf, 180, 0)
    elif up2=="Y":
        player2_index += 0.1
        if player2_index < 4:
            player2_index = 5
        if player2_index >= 6:
            player2_index = 4
        Player2_surf = Player2walk[int(player2_index)]
        Player2_surf = pygame.transform.scale(Player2_surf, PlayerImgSize)
    else:
        player2_index += 0.1
        if player2_index < 6:
            player2_index = 6
        if player2_index >= 9:
            player2_index = 6
        Player2_surf = Player2walk[int(player2_index)]
        Player2_surf = pygame.transform.scale(Player2_surf, PlayerImgSize)
#def Environment_Collision():
    #player1
    #bun table



def npc():
    global npctag
    npctag.append[len(npctag) + 1]
    if random.randint == 1:
        print()




pygame.init()
pygame.display.set_caption("Whatcha' Makin'?")
GroundImgSize = (1000, 1000)
PlayerImgSize = (100, 100)
clock = pygame.time.Clock()
ground_surf = pygame.image.load('graphics/Wood_Tiling.png').convert_alpha()

test_font = pygame.font.Font(None ,50)
test_font2 = pygame.font.SysFont('font/Pixeltype' ,70)


#end screen ticket
EndScreenTicket = pygame.image.load('graphics/End_Ticket.png').convert_alpha()
EndScreen_rect = P1inv_rect = EndScreenTicket.get_rect(midbottom = (0,0))


#Players inv
P1inv = pygame.image.load('graphics/P1_inv.png').convert_alpha()
P1inv_rect = P1inv.get_rect(midbottom = (40,100))
P1inv = pygame.transform.scale(P1inv, (130,130))
P1items_nothing = pygame.image.load('graphics/None.png').convert_alpha()
P1items_RawBurger = pygame.image.load('graphics/Raw_Burger.png').convert_alpha()
P1items_CookedBurger = pygame.image.load('graphics/Cooked_Burger.png').convert_alpha()
P1items_Lettuce = pygame.image.load('graphics/Lettuce.png').convert_alpha()
P1items_Bun = pygame.image.load('graphics/Bun.png').convert_alpha()
P1items_P2 = pygame.image.load('graphics/2Patty.png').convert_alpha()
P1items_P2L = pygame.image.load('graphics/2Patty&Lettuce.png').convert_alpha()
P1items_PL = pygame.image.load('graphics/1Patty&Lettuce.png').convert_alpha()
P1items_RP = pygame.image.load('graphics/Raw_Pizza.png').convert_alpha()
P1items_RCP = pygame.image.load('graphics/Raw_CheesePizza.png').convert_alpha()
P1items_CP = pygame.image.load('graphics/CheesePizza.png').convert_alpha()
P1items_CPB = pygame.image.load('graphics/CheesePizza_Beef.png').convert_alpha()
P1items_CPP = pygame.image.load('graphics/CheesePizza_Pepperoni.png').convert_alpha()
P1items_CPBP = pygame.image.load('graphics/CheesePizza_Beef&Pepperoni.png').convert_alpha()

P1items_Dough = pygame.image.load('graphics/Raw_Dough.png').convert_alpha()
P1items_Chopped_Beef = pygame.image.load('graphics/Chopped_Beef.png').convert_alpha()
P1items_Sauce = pygame.image.load('graphics/Sauce.png').convert_alpha()

P1items_RedSoda = pygame.image.load('graphics/RSoda.png').convert_alpha()
P1items_BlueSoda = pygame.image.load('graphics/BSoda.png').convert_alpha()
P1items_TealSoda = pygame.image.load('graphics/GSoda.png').convert_alpha()
P1items_PinkSoda = pygame.image.load('graphics/PSoda.png').convert_alpha()

P1items_Potato = pygame.image.load('graphics/Potato.png').convert_alpha()
P1items_UncookedFries = pygame.image.load('graphics/UncookedFries.png').convert_alpha()
P1items_Fries = pygame.image.load('graphics/CookedFries.png').convert_alpha()


P1item = [P1items_nothing, P1items_RawBurger, P1items_CookedBurger, P1items_Lettuce, P1items_Bun, 
          P1items_P2, P1items_P2L, P1items_PL, P1items_Dough, P1items_Chopped_Beef, P1items_Sauce, 
          P1items_RedSoda, P1items_BlueSoda, P1items_TealSoda, P1items_PinkSoda, P1items_RP,
           P1items_RCP, P1items_CP, P1items_CPB, P1items_CPP, P1items_CPB, P1items_Potato,
             P1items_UncookedFries, P1items_Fries]



P1item_surf = P1item[P1invID]
P1items_rect = P1item_surf.get_rect(midbottom = (40, 100))
P1item_surf = pygame.transform.scale(P1item_surf, (530,530))

P1item2 = [P1items_nothing, P1items_RawBurger, P1items_CookedBurger, P1items_Lettuce, P1items_Bun, 
          P1items_P2, P1items_P2L, P1items_PL, P1items_Dough, P1items_Chopped_Beef, P1items_Sauce, 
          P1items_RedSoda, P1items_BlueSoda, P1items_TealSoda, P1items_PinkSoda, P1items_RP,
           P1items_RCP, P1items_CP, P1items_CPB, P1items_CPP, P1items_CPB, P1items_Potato,
             P1items_UncookedFries, P1items_Fries]

P1item2_surf = P1item2[P1inv2ID]
P1items2_rect = P1item2_surf.get_rect(midbottom = (130, 85))
P1item2_surf = pygame.transform.scale(P1item2_surf, (530,530))


P1inv2 = pygame.image.load('graphics/P1_inv2.png').convert_alpha()
P1inv2_rect = P1inv2.get_rect(midbottom = (160,150))
P1inv2 = pygame.transform.scale(P1inv2, (70,70))

P2inv = pygame.image.load('graphics/P1_inv.png').convert_alpha()
P2inv_rect = P2inv.get_rect(midbottom = (40,240))
P2inv = pygame.transform.scale(P2inv, (130,130))
P2items_nothing = pygame.image.load('graphics/None.png').convert_alpha()
P2items_RawBurger = pygame.image.load('graphics/Raw_Burger.png').convert_alpha()
P2items_CookedBurger = pygame.image.load('graphics/Cooked_Burger.png').convert_alpha()
P2items_Lettuce = pygame.image.load('graphics/Lettuce.png').convert_alpha()
P2items_Bun = pygame.image.load('graphics/Bun.png').convert_alpha()
P2items_P2 = pygame.image.load('graphics/2Patty.png').convert_alpha()
P2items_P2L = pygame.image.load('graphics/2Patty&Lettuce.png').convert_alpha()
P2items_PL = pygame.image.load('graphics/1Patty&Lettuce.png').convert_alpha()

P2items_Dough = pygame.image.load('graphics/Raw_Dough.png').convert_alpha()
P2items_Chopped_Beef = pygame.image.load('graphics/Chopped_Beef.png').convert_alpha()
P2items_Sauce = pygame.image.load('graphics/Sauce.png').convert_alpha()

P2items_RedSoda = pygame.image.load('graphics/RSoda.png').convert_alpha()
P2items_BlueSoda = pygame.image.load('graphics/BSoda.png').convert_alpha()
P2items_TealSoda = pygame.image.load('graphics/GSoda.png').convert_alpha()
P2items_PinkSoda = pygame.image.load('graphics/PSoda.png').convert_alpha()

P2items_RP = pygame.image.load('graphics/Raw_Pizza.png').convert_alpha()
P2items_RCP = pygame.image.load('graphics/Raw_CheesePizza.png').convert_alpha()
P2items_CP = pygame.image.load('graphics/CheesePizza.png').convert_alpha()
P2items_CPB = pygame.image.load('graphics/CheesePizza_Beef.png').convert_alpha()
P2items_CPP = pygame.image.load('graphics/CheesePizza_Pepperoni.png').convert_alpha()
P2items_CPBP = pygame.image.load('graphics/CheesePizza_Beef&Pepperoni.png').convert_alpha()

P2items_Potato = pygame.image.load('graphics/Potato.png').convert_alpha()
P2items_UncookedFries = pygame.image.load('graphics/UncookedFries.png').convert_alpha()
P2items_Fries = pygame.image.load('graphics/CookedFries.png').convert_alpha()

P2item = [P2items_nothing, P2items_RawBurger, P2items_CookedBurger, P2items_Lettuce, P2items_Bun,
          P2items_P2, P2items_P2L, P2items_PL,P2items_Dough, P2items_Chopped_Beef, P2items_Sauce,
          P2items_RedSoda, P2items_BlueSoda, P2items_TealSoda, P2items_PinkSoda, P2items_RP, P2items_RCP,
          P2items_CP, P2items_CPB, P2items_CPP, P2items_CPBP, P2items_Potato, P2items_UncookedFries, 
          P2items_Fries]

P2item_surf = P2item[P2invID]
P2items_rect = P2item_surf.get_rect(midbottom = (40, 100))
P2item_surf = pygame.transform.scale(P2item_surf, (530,530))


P2inv = pygame.image.load('graphics/P2_inv.png').convert_alpha()
P2inv_rect = P2inv.get_rect(midbottom = (40,240))
P2inv = pygame.transform.scale(P2inv, (130,130))

P2inv2 = pygame.image.load('graphics/P2_inv2.png').convert_alpha()
P2inv2_rect = P1inv.get_rect(midbottom = (160,290))
P2inv2 = pygame.transform.scale(P2inv2, (70,70))

P2item2 = [P1items_nothing, P1items_RawBurger, P1items_CookedBurger, P1items_Lettuce, P1items_Bun, 
          P1items_P2, P1items_P2L, P1items_PL, P1items_Dough, P1items_Chopped_Beef, P1items_Sauce, 
          P1items_RedSoda, P1items_BlueSoda, P1items_TealSoda, P1items_PinkSoda, P1items_RP,
           P1items_RCP, P1items_CP, P1items_CPB, P1items_CPP, P1items_CPB, P1items_Potato,
             P1items_UncookedFries, P1items_Fries]

P2item2_surf = P2item2[P2inv2ID]
P2items2_rect = P2item2_surf.get_rect(midbottom = (130, 225))
P2item2_surf = pygame.transform.scale(P2item2_surf, (530,530))

#Tickets
Nothing = pygame.image.load('graphics/None.png').convert_alpha()
Ticket_PL = pygame.image.load('graphics/ORDER_SWL.png').convert_alpha()
Ticket_2PL = pygame.image.load('graphics/ORDER_DWL.png').convert_alpha()
Ticket_D = pygame.image.load('graphics/ORDER_D.png').convert_alpha()

Ticket_BPS = pygame.image.load('graphics/ORDER_BPWS.png').convert_alpha()
Ticket_BP = pygame.image.load('graphics/ORDER_BP.png').convert_alpha()
Ticket_CP = pygame.image.load('graphics/ORDER_CP.png').convert_alpha()
Ticket_S = pygame.image.load('graphics/ORDER_S.png').convert_alpha()
Ticket_RS = pygame.image.load('graphics/ORDER_RS.png').convert_alpha()
Ticket_TS = pygame.image.load('graphics/ORDER_TS.png').convert_alpha()
Ticket_PS = pygame.image.load('graphics/ORDER_PS.png').convert_alpha()


Ticket_F = pygame.image.load('graphics/ORDER_F.png').convert_alpha()
Ticket_PLF = pygame.image.load('graphics/ORDER_SWLWF.png').convert_alpha()




NPC1_ticket_sprites = [Nothing, Ticket_PL, Ticket_2PL, Ticket_D]
NPC1_ticket_surf = NPC1_ticket_sprites[NPC1_order]
NPC1_ticket_rect = NPC1_ticket_surf.get_rect(midbottom = (300,600))

NPC2_ticket_sprites = [Nothing, Ticket_PL, Ticket_2PL, Ticket_D]
NPC2_ticket_surf = NPC2_ticket_sprites[NPC2_order]
NPC2_ticket_rect = NPC2_ticket_surf.get_rect(midbottom = (300,600))

NPC3_ticket_sprites = [Nothing, Ticket_BPS, Ticket_BP, Ticket_CP, Ticket_S]
NPC3_ticket_surf = NPC3_ticket_sprites[NPC3_order]
NPC3_ticket_rect = NPC3_ticket_surf.get_rect(midbottom = (300,600))

NPC4_ticket_sprites = [Nothing, Ticket_BPS, Ticket_BP, Ticket_CP, Ticket_S, Ticket_PL, Ticket_2PL]
NPC4_ticket_surf = NPC4_ticket_sprites[NPC4_order]
NPC4_ticket_rect = NPC4_ticket_surf.get_rect(midbottom = (300,600))

NPC5_ticket_sprites = [Nothing, Ticket_PLF, Ticket_F, Ticket_PL, Ticket_S, Ticket_RS, Ticket_TS, Ticket_PS]
NPC5_ticket_surf = NPC5_ticket_sprites[NPC5_order]
NPC5_ticket_rect = NPC5_ticket_surf.get_rect(midbottom = (300,600))

#NPC's
NPC_Empty = pygame.image.load('graphics/NPCs/NPc_Empty.png').convert_alpha()
#Dino dud
Dino_Stand = pygame.image.load('graphics/NPCs/NPC_Dino(stand).png').convert_alpha()
Dino_Stand2 = pygame.image.load('graphics/NPCs/NPC_Dino(stand2).png').convert_alpha()
Dino_Down = pygame.image.load('graphics/NPCs/NPC_Dino(down).png').convert_alpha()
Dino_Down2 = pygame.image.load('graphics/NPCs/NPC_Dino(down2).png').convert_alpha()
Dino_Up = pygame.image.load('graphics/NPCs/NPC_Dino(up).png').convert_alpha()
Dino_Up2 = pygame.image.load('graphics/NPCs/NPC_Dino(up2).png').convert_alpha()
Dino_LR = pygame.image.load('graphics/NPCs/NPC_Dino(LR).png').convert_alpha()
Dino_LR2 = pygame.image.load('graphics/NPCs/NPC_Dino(LR2).png').convert_alpha()
Dino_NPC_sprites = [Dino_Stand, Dino_Stand2, Dino_Down, Dino_Down2, Dino_Up, Dino_Up2,
                 Dino_LR, Dino_LR2,NPC_Empty]
NPC1_surf = Dino_NPC_sprites[NPC1_index]
NPC1_rect = NPC1_surf.get_rect(midbottom = (300, 600))
NPC1_mask = pygame.mask.from_surface(NPC1_surf)

#Patch
Patch_Stand = pygame.image.load('graphics/NPCs/NPC_Patch(stand).png').convert_alpha()
Patch_Stand2 = pygame.image.load('graphics/NPCs/NPC_Patch(stand2).png').convert_alpha()
Patch_Down = pygame.image.load('graphics/NPCs/NPC_Patch(down).png').convert_alpha()
Patch_Down2 = pygame.image.load('graphics/NPCs/NPC_Patch(down2).png').convert_alpha()
Patch_Up = pygame.image.load('graphics/NPCs/NPC_Patch(up).png').convert_alpha()
Patch_Up2 = pygame.image.load('graphics/NPCs/NPC_Patch(up2).png').convert_alpha()
Patch_LR = pygame.image.load('graphics/NPCs/NPC_Patch(LR).png').convert_alpha()
Patch_LR2 = pygame.image.load('graphics/NPCs/NPC_Patch(LR2).png').convert_alpha()
Patch_NPC_sprites = [Patch_Stand, Patch_Stand2, Patch_Down, Patch_Down2, Patch_Up,
                  Patch_Up2, Patch_LR, Patch_LR2, NPC_Empty]
NPC2_surf = Patch_NPC_sprites[NPC2_index]
NPC2_rect = NPC2_surf.get_rect(midbottom = (500, 600))
NPC2_mask = pygame.mask.from_surface(NPC2_surf)

#Jason
Jason_Stand = pygame.image.load('graphics/NPCs/NPC_Jason(stand).png').convert_alpha()
Jason_Stand2 = pygame.image.load('graphics/NPCs/NPC_Jason(stand2).png').convert_alpha()
Jason_Down = pygame.image.load('graphics/NPCs/NPC_Jason(down).png').convert_alpha()
Jason_Down2 = pygame.image.load('graphics/NPCs/NPC_Jason(down2).png').convert_alpha()
Jason_Up = pygame.image.load('graphics/NPCs/NPC_Jason(up).png').convert_alpha()
Jason_Up2 = pygame.image.load('graphics/NPCs/NPC_Jason(up2).png').convert_alpha()
Jason_LR = pygame.image.load('graphics/NPCs/NPC_Jason(LR).png').convert_alpha()
Jason_LR2 = pygame.image.load('graphics/NPCs/NPC_Jason(LR2).png').convert_alpha()
Jason_NPC_sprites = [Jason_Stand, Jason_Stand2, Jason_Down, Jason_Down2, Jason_Up,
                  Jason_Up2, Jason_LR, Jason_LR2, NPC_Empty]
NPC3_surf = Jason_NPC_sprites[NPC3_index]
NPC3_rect = NPC3_surf.get_rect(midbottom = (100, 600))
NPC3_mask = pygame.mask.from_surface(NPC3_surf)

#Cryptid
Cryptid_Stand = pygame.image.load('graphics/NPCs/NPC_Cryptid(stand).png').convert_alpha()
Cryptid_Stand2 = pygame.image.load('graphics/NPCs/NPC_Cryptid(stand2).png').convert_alpha()
Cryptid_Down = pygame.image.load('graphics/NPCs/NPC_Cryptid(down).png').convert_alpha()
Cryptid_Down2 = pygame.image.load('graphics/NPCs/NPC_Cryptid(down2).png').convert_alpha()
Cryptid_Up = pygame.image.load('graphics/NPCs/NPC_Cryptid(up).png').convert_alpha()
Cryptid_Up2 = pygame.image.load('graphics/NPCs/NPC_Cryptid(up2).png').convert_alpha()
Cryptid_LR = pygame.image.load('graphics/NPCs/NPC_Cryptid(LR).png').convert_alpha()
Cryptid_LR2 = pygame.image.load('graphics/NPCs/NPC_Cryptid(LR2).png').convert_alpha()
Cryptid_NPC_sprites = [Cryptid_Stand, Cryptid_Stand2, Cryptid_Down, Cryptid_Down2, Cryptid_Up,
                  Cryptid_Up2, Cryptid_LR, Cryptid_LR2, NPC_Empty]
NPC4_surf = Cryptid_NPC_sprites[NPC4_index]
NPC4_rect = NPC4_surf.get_rect(midbottom = (800, 600))
NPC4_mask = pygame.mask.from_surface(NPC4_surf)

#Chiaki
Chiaki_Stand = pygame.image.load('graphics/NPCs/NPC_Chiaki(stand).png').convert_alpha()
Chiaki_Stand2 = pygame.image.load('graphics/NPCs/NPC_Chiaki(stand2).png').convert_alpha()
Chiaki_Down = pygame.image.load('graphics/NPCs/NPC_Chiaki(down).png').convert_alpha()
Chiaki_Down2 = pygame.image.load('graphics/NPCs/NPC_Chiaki(down2).png').convert_alpha()
Chiaki_Up = pygame.image.load('graphics/NPCs/NPC_Chiaki(up).png').convert_alpha()
Chiaki_Up2 = pygame.image.load('graphics/NPCs/NPC_Chiaki(up2).png').convert_alpha()
Chiaki_LR = pygame.image.load('graphics/NPCs/NPC_Chiaki(LR).png').convert_alpha()
Chiaki_LR2 = pygame.image.load('graphics/NPCs/NPC_Chiaki(LR2).png').convert_alpha()
Chiaki_NPC_sprites = [Chiaki_Stand, Chiaki_Stand2, Chiaki_Down, Chiaki_Down2, Chiaki_Up, Chiaki_Up2,
                 Chiaki_LR, Chiaki_LR2,NPC_Empty]
NPC5_surf = Chiaki_NPC_sprites[NPC5_index]
NPC5_rect = NPC5_surf.get_rect(midbottom = (300, 600))
NPC5_mask = pygame.mask.from_surface(NPC5_surf)

#Sodas
BlueSoda = pygame.image.load('graphics/BlueSoda.png').convert_alpha()
RedSoda = pygame.image.load('graphics/RedSoda.png').convert_alpha()
TealSoda = pygame.image.load('graphics/TealSoda.png').convert_alpha()
PinkSoda = pygame.image.load('graphics/PinkSoda.png').convert_alpha()

BlueSoda_rect = BlueSoda.get_rect(midbottom = (800, 400))
BlueSoda_mask = pygame.mask.from_surface(BlueSoda)

RedSoda_rect = RedSoda.get_rect(midbottom = (850, 400))
RedSoda_mask = pygame.mask.from_surface(RedSoda)

TealSoda_rect = TealSoda.get_rect(midbottom = (900, 400))
TealSoda_mask = pygame.mask.from_surface(TealSoda)

PinkSoda_rect = PinkSoda.get_rect(midbottom = (950, 400))
PinkSoda_mask = pygame.mask.from_surface(PinkSoda)

#stove 
stoveOn = pygame.image.load('graphics/stove[On].png').convert_alpha()
stoveOff = pygame.image.load('graphics/stove[Off].png').convert_alpha()
StoveSprites = [stoveOff, stoveOn]
stove_surf = StoveSprites[StoveAnimation]
stove_rect = stove_surf.get_rect(midbottom= (400,200))
stove_mask = pygame.mask.from_surface(stove_surf)
stoveMaskImage = stove_mask.to_surface()

#stove 2
stove2On = pygame.image.load('graphics/stove[On].png').convert_alpha()
stove2Off = pygame.image.load('graphics/stove[Off].png').convert_alpha()
Stove2Sprites = [stove2Off, stove2On]
stove2_surf = Stove2Sprites[Stove2Animation]
stove2_rect = stove2_surf.get_rect(midbottom= (500,200))
stove2_mask = pygame.mask.from_surface(stove2_surf)
stove2MaskImage = stove2_mask.to_surface()

#stove timer
Stove1_VT0 = pygame.image.load('graphics/StoveTimer/stovetimer[0].png').convert_alpha()
Stove1_VT1 = pygame.image.load('graphics/StoveTimer/stovetimer[1].png').convert_alpha()
Stove1_VT2 = pygame.image.load('graphics/StoveTimer/stovetimer[2].png').convert_alpha()
Stove1_VT3 = pygame.image.load('graphics/StoveTimer/stovetimer[3].png').convert_alpha()
Stove1_VT4 = pygame.image.load('graphics/StoveTimer/stovetimer[4].png').convert_alpha()
Stove1_VT5 = pygame.image.load('graphics/StoveTimer/stovetimer[5].png').convert_alpha()
Stove1_VT6 = pygame.image.load('graphics/StoveTimer/stovetimer[6].png').convert_alpha()
Stove1_VT7 = pygame.image.load('graphics/StoveTimer/stovetimer[7].png').convert_alpha()
Stove1_VT8 = pygame.image.load('graphics/StoveTimer/stovetimer[8].png').convert_alpha()
Stove1_VT9 = pygame.image.load('graphics/StoveTimer/stovetimer[9].png').convert_alpha()
Stove1_VT10 = pygame.image.load('graphics/StoveTimer/stovetimer[10].png').convert_alpha()
Stove1_VT11 = pygame.image.load('graphics/StoveTimer/stovetimer[11].png').convert_alpha()
Stove1_VT12 = pygame.image.load('graphics/StoveTimer/stovetimer[12].png').convert_alpha()
Stove1_VT13 = pygame.image.load('graphics/StoveTimer/stovetimer[13].png').convert_alpha()
Stove1_VT14 = pygame.image.load('graphics/StoveTimer/stovetimer[14].png').convert_alpha()
Stove1_VTNA = pygame.image.load('graphics/StoveTimer/stovetimer[None].png').convert_alpha()
stove1_VT_sprites = [Stove1_VT0, Stove1_VT1, Stove1_VT2, Stove1_VT3, Stove1_VT4, Stove1_VT5,
                  Stove1_VT6, Stove1_VT7, Stove1_VT8, Stove1_VT9, Stove1_VT10, Stove1_VT11, 
                  Stove1_VT12, Stove1_VT13, Stove1_VT14, Stove1_VTNA]
stove1_VT_surf = stove1_VT_sprites[StoveTimerStage]
stove1_VT_rect = stove1_VT_surf.get_rect(midbottom = (410, 120))

#stove timer

stove2_VT_sprites = [Stove1_VT0, Stove1_VT1, Stove1_VT2, Stove1_VT3, Stove1_VT4, Stove1_VT5,
                  Stove1_VT6, Stove1_VT7, Stove1_VT8, Stove1_VT9, Stove1_VT10, Stove1_VT11, 
                  Stove1_VT12, Stove1_VT13, Stove1_VT14, Stove1_VTNA]
stove2_VT_surf = stove2_VT_sprites[StoveTimerStage]
stove2_VT_rect = stove2_VT_surf.get_rect(midbottom = (510, 120))

#Fryer
fryer = pygame.image.load('graphics/fryer.png').convert_alpha()
fryerSprites = [fryer]
fryer_surf = fryerSprites[0]
fryer_rect = fryer_surf.get_rect(midbottom= (180,190))
fryer_mask = pygame.mask.from_surface(fryer_surf)
fryerMaskImage = fryer_mask.to_surface()

#Fryer VT
fryer1_VT_sprites = [Stove1_VT0, Stove1_VT1, Stove1_VT2, Stove1_VT3, Stove1_VT4, Stove1_VT5,
                  Stove1_VT6, Stove1_VT7, Stove1_VT8, Stove1_VT9, Stove1_VT10, Stove1_VT11, 
                  Stove1_VT12, Stove1_VT13, Stove1_VT14, Stove1_VTNA]
fryer1_VT_surf = fryer1_VT_sprites[fryerTimerStage]
fryer1_VT_rect = fryer1_VT_surf.get_rect(midbottom = (230, 130))

#Dough & Sauce wombo combo
doughtable_surf = pygame.image.load('graphics/DoughCounter.png').convert_alpha()
doughtable_rect = doughtable_surf.get_rect(midbottom = (250,350))
doughtable_surf = pygame.transform.scale(doughtable_surf, (250,250))
dough_mask = pygame.mask.from_surface(doughtable_surf)
DoughMaskImage = dough_mask.to_surface()

saucetable_surf = pygame.image.load('graphics/SauceCounter.png').convert_alpha()
saucetable_rect = saucetable_surf.get_rect(midbottom = (420,350))
saucetable_surf = pygame.transform.scale(saucetable_surf, (250,250))
sauce_mask = pygame.mask.from_surface(saucetable_surf)
SauceMaskImage = sauce_mask.to_surface()

cuttingtable_surf = pygame.image.load('graphics/CuttingCounter.png').convert_alpha()
cuttingtable_rect = cuttingtable_surf.get_rect(midbottom = (330,350))
cuttingtable_surf = pygame.transform.scale(cuttingtable_surf, (250,250))
cuttingtable_mask = pygame.mask.from_surface(cuttingtable_surf)
CuttingMaskImage = cuttingtable_mask.to_surface()

#Potato
potatotable_surf = pygame.image.load('graphics/potatoCounter.png').convert_alpha()
potatotable_rect = potatotable_surf.get_rect(midbottom = (500,380))
potatotable_surf = pygame.transform.scale(potatotable_surf, (200,200))
potatotable_mask = pygame.mask.from_surface(potatotable_surf)
potatoMaskImage = potatotable_mask.to_surface()

#Trash skrub
trash_surf = pygame.image.load('graphics/Trash.png').convert_alpha()
trash_rect = trash_surf.get_rect(midbottom = (800, 200))
trash_surf = pygame.transform.scale(trash_surf, (150,150))
trash_mask = pygame.mask.from_surface(trash_surf)
trashMaskImage = trash_mask.to_surface()

#Burger counter stand
beeftable_surf = pygame.image.load('graphics/BeefCounter.png').convert_alpha()
beeftable_rect = beeftable_surf.get_rect(midbottom = (630,190))
beeftable_surf = pygame.transform.scale(beeftable_surf, (200,200))
beeftable_mask = pygame.mask.from_surface(beeftable_surf)
beeftableMaskImage = beeftable_mask.to_surface()

#Lettuce counter stand
lettucetable_surf = pygame.image.load('graphics/LettuceCounter.png').convert_alpha()
lettucetable_rect = lettucetable_surf.get_rect(midbottom = (570,190))
lettucetable_surf = pygame.transform.scale(lettucetable_surf, (200,200))
lettucetable_mask = pygame.mask.from_surface(lettucetable_surf)
lettucetableMaskImage = lettucetable_mask.to_surface()

#Cheese table
cheesetable_surf = pygame.image.load('graphics/Cheesetable.png').convert_alpha()
cheesetable_rect = cheesetable_surf.get_rect(midbottom = (190,380))
cheesetable_surf = pygame.transform.scale(cheesetable_surf, (200,200))
cheesetable_mask = pygame.mask.from_surface(cheesetable_surf)
cheesetableMaskImage = cheesetable_mask.to_surface()


#bun counter stand
buntable_surf = pygame.image.load('graphics/BunCounter.png').convert_alpha()
buntable_rect = buntable_surf.get_rect(midbottom = (700,190))
buntable_surf = pygame.transform.scale(buntable_surf, (200,200))
buntable_mask = pygame.mask.from_surface(buntable_surf)
buntableMaskImage = buntable_mask.to_surface()

#Chopped Beef station
ChoppedBeeftable_empty_surf = pygame.image.load('graphics/ChoppedBeefCounter(empty).png').convert_alpha()
ChoppedBeeftable_full_surf = pygame.image.load('graphics/ChoppedBeefCounter(full).png').convert_alpha()
ChoppedBeeftable_sprites = [ChoppedBeeftable_full_surf, ChoppedBeeftable_empty_surf]
ChoppedBeeftable_surf = ChoppedBeeftable_sprites[1]
ChoppedBeeftable_rect = ChoppedBeeftable_surf.get_rect(midbottom = (550,380))
ChoppedBeeftable_mask = pygame.mask.from_surface(ChoppedBeeftable_surf)

#burger making stand
BMS_empty =  pygame.image.load('graphics/BurgerMakingStation/BMS[Empty].png').convert_alpha()
BMS_B =  pygame.image.load('graphics/BurgerMakingStation/BMS[Bun].png').convert_alpha()
BMS_BP =  pygame.image.load('graphics/BurgerMakingStation/BMS[Bun+Patty].png').convert_alpha()
BMS_BPL =  pygame.image.load('graphics/BurgerMakingStation/BMS[Bun+Patty+Lettuce].png').convert_alpha()
BMS_B2PL =  pygame.image.load('graphics/BurgerMakingStation/BMS[Bun2+Patty+Lettuce].png').convert_alpha()
BMS_BP2 =  pygame.image.load('graphics/BurgerMakingStation/BMS[Bun+Patty2].png').convert_alpha()
BMS_B2P2 =  pygame.image.load('graphics/BurgerMakingStation/BMS[Bun2+Patty2].png').convert_alpha()
BMS_BP2L =  pygame.image.load('graphics/BurgerMakingStation/BMS[Bun+Patty2+Lettuce].png').convert_alpha()
BMS_B2P2L =  pygame.image.load('graphics/BurgerMakingStation/BMS[Bun2+Patty2+Lettuce].png').convert_alpha()

#None 1 #Bun 1 #Bun patty 2 #Bun Patty Lettuce 3 #




BMS_sprites = [BMS_empty, BMS_B, BMS_BP, BMS_BPL, BMS_B2PL, BMS_BP2, BMS_B2P2, BMS_BP2L, BMS_B2P2L]
BMS_surf = BMS_sprites[StoveTimerStage]
BMS_rect = BMS_surf.get_rect(midbottom = (260, 150))
BMS_mask = pygame.mask.from_surface(BMS_surf)
BMS_surf = pygame.transform.scale(BMS_surf,(150,150))

#Players
Player1walk1 =  pygame.image.load('graphics/Chef1(Walk).png').convert_alpha()
Player1walk2 =  pygame.image.load('graphics/Chef1(Walk2).png').convert_alpha()
Player1walk3 = pygame.image.load('graphics/Chef1(right).png').convert_alpha()
Player1walk4 = pygame.image.load('graphics/Chef1(right2).png').convert_alpha()
Player1walk5 = pygame.image.load('graphics/Chef1(Up).png').convert_alpha()
Player1walk6 = pygame.image.load('graphics/Chef1(Up2).png').convert_alpha()
Player1stand1 = pygame.image.load('graphics/Chef1(stand).png').convert_alpha()
Player1stand2 = pygame.image.load('graphics/Chef1(stand2).png').convert_alpha()
Player1stand3 = pygame.image.load('graphics/Chef1(stand3).png').convert_alpha()

Player2walk1 =  pygame.image.load('graphics/Chef2(Walk).png').convert_alpha()
Player2walk2 =  pygame.image.load('graphics/Chef2(Walk2).png').convert_alpha()
Player2walk3 = pygame.image.load('graphics/Chef2(right).png').convert_alpha()
Player2walk4 = pygame.image.load('graphics/Chef2(right2).png').convert_alpha()
Player2walk5 = pygame.image.load('graphics/Chef2(Up).png').convert_alpha()
Player2walk6 = pygame.image.load('graphics/Chef2(Up2).png').convert_alpha()
Player2stand1 = pygame.image.load('graphics/Chef2(stand).png').convert_alpha()
Player2stand2 = pygame.image.load('graphics/Chef2(stand2).png').convert_alpha()
Player2stand3 = pygame.image.load('graphics/Chef2(stand3).png').convert_alpha()



Player1walk = [Player1walk1, Player1walk2, Player1walk3, Player1walk4, Player1walk5, Player1walk6, Player1stand1, Player1stand2, Player1stand3]
Player1_surf = Player1walk[player_index]

Player1_rect = Player1_surf.get_rect(midbottom = (500, 100)).scale_by(0.45,0.5)
Player1_mask = pygame.mask.from_surface(Player1_surf)
mask_image = Player1_mask.to_surface()



#print(StoveSprites[0])
Player2walk = [Player2walk1, Player2walk2, Player2walk3, Player2walk4, Player2walk5, Player2walk6, Player2stand1, Player2stand2, Player2stand3]
Player2_surf = Player2walk[player_index]
Player2_mask = pygame.mask.from_surface(Player2_surf)
mask_image2 = Player2_mask.to_surface()


Player2_rect = Player2_surf.get_rect(midbottom = (400, 100)).scale_by(0.45,0.45)

ground_surf = pygame.transform.scale(ground_surf, GroundImgSize)

Player1_surf = pygame.transform.scale(Player1_surf, PlayerImgSize)

value = 0
speed = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  
    
    NPC1_ticket_rect.y = NPC1_rect.y+100
    NPC1_ticket_rect.x = NPC1_rect.x
    NPC2_ticket_rect.y = NPC2_rect.y+100
    NPC2_ticket_rect.x = NPC2_rect.x
    NPC3_ticket_rect.y = NPC3_rect.y+100
    NPC3_ticket_rect.x = NPC3_rect.x
    NPC4_ticket_rect.y = NPC4_rect.y+100
    NPC4_ticket_rect.x = NPC4_rect.x
    NPC5_ticket_rect.y = NPC5_rect.y+100
    NPC5_ticket_rect.x = NPC5_rect.x
    
    
    Time -= .01

    keys = pygame.key.get_pressed()
    #Player1 Controls
    if keys [pygame.K_d]:
        Player1_rect.x += 2
        if Player1_mask.overlap(Player2_mask, (Player2_rect.x - Player1_rect.x, Player2_rect.y - Player1_rect.y)):
            Player1_rect.x -= 2
        right="Y"
    else:
        right="N"
    if keys [pygame.K_a]:
        Player1_rect.x -= 2
        if Player1_mask.overlap(Player2_mask, (Player2_rect.x - Player1_rect.x, Player2_rect.y - Player1_rect.y)):
            Player1_rect.x += 2
        left="Y"
    else:
        left="N"
    if keys [pygame.K_w]:
        Player1_rect.y -= 2
        if Player1_mask.overlap(Player2_mask, (Player2_rect.x - Player1_rect.x, Player2_rect.y - Player1_rect.y)):
            Player1_rect.y += 2
        up="Y"
    else:
        up="N"
    if keys [pygame.K_s]:
        Player1_rect.y += 2
        if Player1_mask.overlap(Player2_mask, (Player2_rect.x - Player1_rect.x, Player2_rect.y - Player1_rect.y)):
            Player1_rect.y -= 2
        down="Y"
    else:
        down="N"
    
    #Borders
    if True:
        if Player1_rect.x > 930:
            Player1_rect.x = 930
        if Player1_rect.x < -30:
            Player1_rect.x = -30
        if Player1_rect.y < -16:
            Player1_rect.y = -16
        if Player1_rect.y > 760:
            Player1_rect.y = 760

        if Player2_rect.x > 930:
            Player2_rect.x = 930
        if Player2_rect.x < -30:
            Player2_rect.x = -30
        if Player2_rect.y < -16:
            Player2_rect.y = -16
        if Player2_rect.y > 760:
            Player2_rect.y = 760
        
        if NPC1_rect.x > 930:
            NPC1_rect.x = 930
        if NPC1_rect.x < -30:
            NPC1_rect.x = -30
        if NPC1_rect.y < 306:
            NPC1_rect.y = 306
        if NPC1_rect.y > 600:
            NPC1_rect.y = 600
        
        if NPC2_rect.x > 930:
            NPC2_rect.x = 930
        if NPC2_rect.x < -30:
            NPC2_rect.x = -30
        if NPC2_rect.y < 306:
            NPC2_rect.y = 306
        if NPC2_rect.y > 600:
            NPC2_rect.y = 600

        if NPC3_rect.x > 930:
            NPC3_rect.x = 930
        if NPC3_rect.x < -30:
            NPC3_rect.x = -30
        if NPC3_rect.y < 306:
            NPC3_rect.y = 306
        if NPC3_rect.y > 600:
            NPC3_rect.y = 600

        if NPC4_rect.x > 930:
            NPC4_rect.x = 930
        if NPC4_rect.x < -30:
            NPC4_rect.x = -30
        if NPC4_rect.y < 306:
            NPC4_rect.y = 306
        if NPC4_rect.y > 600:
            NPC4_rect.y = 600
        
        if NPC5_rect.x > 930:
            NPC5_rect.x = 930
        if NPC5_rect.x < -30:
            NPC5_rect.x = -30
        if NPC5_rect.y < 306:
            NPC5_rect.y = 306
        if NPC5_rect.y > 600:
            NPC5_rect.y = 600
        
    if keys [pygame.K_e]: #PLAYER 1 INTERACTION KEY
        #NPC1
        if Player1_mask.overlap(NPC1_mask, (NPC1_rect.x - Player1_rect.x, NPC1_rect.y - Player1_rect.y)):
            if player1_inv == 'P&L' and NPC1_order == 1: #[Nothing, Ticket_PL, Ticket_2PL, Ticket_D]
                player1_inv = 'None'
                Score += 5 + random.randint(1,3)
                NPC1_order = 0
                NPC1_order_buffer = 120
                FoodMade +=1
            if player1_inv == '2P&L' and NPC1_order == 2:
                player1_inv = 'None'
                Score += 7 + random.randint (2, 4)
                NPC1_order = 0
                NPC1_order_buffer = 120
                FoodMade +=1
            if player1_inv == '2P' and NPC1_order == 3:
                player1_inv = 'None'
                Score += 6 + random.randint(2,3)
                NPC1_order = 0
                NPC1_order_buffer = 120
                FoodMade +=1

        
        #NPC2
        if Player1_mask.overlap(NPC2_mask, (NPC2_rect.x - Player1_rect.x, NPC2_rect.y - Player1_rect.y)):
            if player1_inv == 'P&L' and NPC2_order == 1: #[Nothing, Ticket_PL, Ticket_2PL, Ticket_D]
                player1_inv = 'None'
                Score += 5 + random.randint(1,3)
                NPC2_order = 0
                NPC2_order_buffer = 120
                FoodMade +=1
            if player1_inv == '2P&L' and NPC2_order == 2:
                player1_inv = 'None'
                Score += 7 + random.randint (2, 4)
                NPC2_order = 0
                NPC2_order_buffer = 120
                FoodMade +=1
            if player1_inv == '2P' and NPC2_order == 3:
                player1_inv = 'None'
                Score += 6 + random.randint(2,3)
                NPC2_order = 0
                NPC2_order_buffer = 120
                FoodMade +=1
        
        #NPC 3
        if Player1_mask.overlap(NPC3_mask, (NPC3_rect.x - Player1_rect.x, NPC3_rect.y - Player1_rect.y)):
            if player1_inv == 'Beef Pizza' and NPC3_order == 1:
                player1_inv = 'None'
                NPC3_order = 4
            if player1_inv == 'Beef Pizza' and NPC3_order == 2:
                player1_inv = 'None'
                NPC3_order = 0
                NPC3_order_buffer = 200
                Score += 20 + random.randint(2,5)
                FoodMade +=1
            if player1_inv == 'Blue Soda' and NPC3_order == 4:
                player1_inv = 'None'
                NPC3_order = 0
                NPC3_order_buffer = 200
                Score += 20 + random.randint(2,5)
                FoodMade +=1
            if player1_inv == 'Blue Soda' and NPC3_order == 1:
                player1_inv = 'None'
                NPC3_order = 2
        
        #NPC 4  #NPC4_ticket_sprites = [Nothing, Ticket_BPS, Ticket_BP, Ticket_CP, Ticket_S, Ticket_PL, Ticket_2PL]
        if Player1_mask.overlap(NPC4_mask, (NPC4_rect.x - Player1_rect.x, NPC4_rect.y - Player1_rect.y)):

            if player1_inv == 'Beef Pizza' and NPC4_order == 1:
                player1_inv = 'None'
                NPC4_order = 4
            if player1_inv == 'Blue Soda' and NPC4_order == 1:
                player1_inv = 'None'
                NPC4_order = 2
            if player1_inv == 'Beef Pizza' and NPC4_order == 2:
                player1_inv = 'None'
                NPC4_order = 0
                NPC4_order_buffer = 150
                Score += 25 + random.randint(1,4)
                FoodMade +=1
            if player1_inv == 'Cheese Pizza' and NPC4_order == 3:
                player1_inv = 'None'
                NPC4_order = 0
                NPC4_order_buffer = 150
                Score += 25 + random.randint(1,4)
                FoodMade +=1
            if player1_inv == 'Blue Soda' and NPC4_order == 4:
                player1_inv = 'None'
                NPC4_order = 0
                NPC4_order_buffer = 150
                Score += 25 + random.randint(1,4)
                FoodMade +=1
            if player1_inv == 'P&L' and NPC4_order == 5:
                player1_inv = 'None'
                NPC4_order = 0
                NPC4_order_buffer = 150
                Score += 15 + random.randint(1,4)
                FoodMade +=1
            if player1_inv == '2P&L' and NPC4_order == 6:
                player1_inv = 'None'
                NPC4_order = 0
                NPC4_order_buffer = 150
                Score += 20 + random.randint(1,4)
                FoodMade +=1
            
            #NPC 5 [Nothing, Ticket_PLF, Ticket_F, Ticket_PL, Ticket_S, Ticket_RS, Ticket_TS, Ticket_PS]
        if Player1_mask.overlap(NPC5_mask, (NPC5_rect.x - Player1_rect.x, NPC5_rect.y - Player1_rect.y)):
            if player1_inv == 'P&L' and NPC5_order == 1:
                player1_inv = 'None'
                NPC5_order = 2
            if player1_inv == 'Fries' and NPC5_order == 2:
                player1_inv = 'None'
                NPC5_order = 0
                NPC5_order_buffer = 100
                Score += 15 + random.randint(1,10)
                FoodMade += 1
            if player1_inv == 'P&L' and NPC5_order == 3:
                player1_inv = 'None'
                NPC5_order = 0
                NPC5_order_buffer = 100
                Score += 15 + random.randint(1,10)
                FoodMade += 1
            if player1_inv == 'Fries' and NPC5_order == 1:
                player1_inv = 'None'
                NPC5_order = 3
            if player1_inv == 'Blue Soda' and NPC5_order == 4:
                player1_inv = 'None'
                NPC5_order = 0
                NPC5_order_buffer = 20
                Score += 3 + random.randint(1,2)
                FoodMade += 1
            if player1_inv == 'Red Soda' and NPC5_order == 5:
                player1_inv = 'None'
                NPC5_order = 0
                NPC5_order_buffer = 20
                Score += 3 + random.randint(1,2)
                FoodMade += 1
            if player1_inv == 'Teal Soda' and NPC5_order == 6:
                player1_inv = 'None'
                NPC5_order = 0
                NPC5_order_buffer = 20
                Score += 3 + random.randint(1,2)
                FoodMade += 1
            if player1_inv == 'Pink Soda' and NPC5_order == 7:
                player1_inv = 'None'
                NPC5_order = 0
                NPC5_order_buffer = 20
                Score += 3 + random.randint(1,2)
                FoodMade += 1
            
        


        #BurgerMakingStation
        if Player1_mask.overlap(BMS_mask, (BMS_rect.x - Player1_rect.x, BMS_rect.y- Player1_rect.y)):
            if BMS_Stand == [] and player1_inv == 'Bun':
                BMS_Stand.append('Bun')
                BMS_surf = BMS_sprites[1]
                player1_inv = 'None'
            elif BMS_Stand == ['Bun'] and player1_inv == 'Cooked Burger':
                BMS_Stand.append('Patty')
                BMS_surf = BMS_sprites[2]
                player1_inv = 'None'
            #Bun Patty Route
            elif BMS_Stand == ['Bun', 'Patty'] and player1_inv == 'Cooked Burger':
                BMS_Stand.append('Patty') #2 Patties
                BMS_surf = BMS_sprites[5]
                player1_inv = 'None'
            elif BMS_Stand == ['Bun', 'Patty'] and player1_inv == 'Lettuce':
                BMS_Stand.append('Lettuce')
                BMS_surf = BMS_sprites[3]
                player1_inv = 'None'
            #Bun Patty Lettuce Bun
            elif BMS_Stand == ['Bun', 'Patty', 'Lettuce'] and player1_inv == 'Bun':
                BMS_Stand.append('Bun')
                BMS_surf = BMS_sprites[4]
                player1_inv = 'None'
            #Bun Patty2
            elif BMS_Stand == ['Bun', 'Patty', 'Patty'] and player1_inv == 'Bun':
                BMS_Stand.append('Bun')
                BMS_surf = BMS_sprites[6]
                player1_inv = 'None'
            elif BMS_Stand == ['Bun', 'Patty', 'Patty'] and player1_inv == 'Lettuce':
                BMS_Stand.append('Lettuce')
                BMS_surf = BMS_sprites[7]
                player1_inv = 'None'
            elif BMS_Stand == ['Bun', 'Patty', 'Patty', 'Lettuce'] and player1_inv == 'Bun':
                BMS_Stand.append('Bun')
                BMS_surf = BMS_sprites[8]
                player1_inv = 'None'
            elif BMS_Stand == ['Bun', 'Patty', 'Patty', 'Bun']:
                BMS_Stand.clear()
                BMS_surf = BMS_sprites[0]
                player1_inv = '2P'
            elif BMS_Stand == ['Bun', 'Patty', 'Patty', 'Lettuce', 'Bun']:
                BMS_Stand.clear()
                BMS_surf = BMS_sprites[0]
                player1_inv = '2P&L'
            elif BMS_Stand == ['Bun', 'Patty', 'Lettuce', 'Bun']:
                BMS_Stand.clear()
                BMS_surf = BMS_sprites[0]
                player1_inv = 'P&L'



        if Player1_mask.overlap(stove_mask, (stove_rect.x - Player1_rect.x, stove_rect.y- Player1_rect.y)):
            if player1_inv == 'Raw Burger' and stove1Slot == 'None':
                Stove1Timer = 30
                stove1Slot = 'Raw Burger'
                player1_inv = 'None'
            elif player1_inv == 'None' and stove1Slot == 'Cooked Burger':
                player1_inv = 'Cooked Burger'
                stove1Slot = 'None'

            if player1_inv == 'Raw Cheese Pizza' and stove1Slot == 'None':
                Stove1Timer = 70
                stove1Slot = 'Raw Cheese Pizza'
                player1_inv = 'None'
            elif player1_inv == 'None' and stove1Slot == 'Cheese Pizza':
                player1_inv = 'Cheese Pizza'
                stove1Slot = 'None'
            
        #Stove 2        
        if Player1_mask.overlap(stove2_mask, (stove2_rect.x - Player1_rect.x, stove2_rect.y- Player1_rect.y)):
            if player1_inv == 'Raw Burger' and stove2Slot == 'None':
                Stove2Timer = 30
                stove2Slot = 'Raw Burger'
                player1_inv = 'None'
            elif player1_inv == 'None' and stove2Slot == 'Cooked Burger':
                player1_inv = 'Cooked Burger'
                stove2Slot = 'None'
            
            if player1_inv == 'Raw Cheese Pizza' and stove2Slot == 'None':
                Stove2Timer = 70
                stove2Slot = 'Raw Cheese Pizza'
                player1_inv = 'None'
            elif player1_inv == 'None' and stove2Slot == 'Cheese Pizza':
                player1_inv = 'Cheese Pizza'
                stove2Slot = 'None'
        #Frier
        if Player1_mask.overlap(fryer_mask, (fryer_rect.x - Player1_rect.x, fryer_rect.y- Player1_rect.y)):
            if player1_inv == 'Raw Fries' and fryer1Slot == 'None':
                fryer1Timer = 40
                fryer1Slot = 'Raw Fries'
                player1_inv = 'None'
        if Player1_mask.overlap(fryer_mask, (fryer_rect.x - Player1_rect.x, fryer_rect.y- Player1_rect.y)):
            if player1_inv == 'None' and fryer1Slot == 'Fries':
                fryer1Slot = 'None'
                player1_inv = 'Fries'
            
            
        #Beef table
        if Player1_mask.overlap(beeftable_mask, (beeftable_rect.x - Player1_rect.x, beeftable_rect.y- Player1_rect.y)):
            if player1_inv == 'None':
                player1_inv = 'Raw Burger'
        if Player1_mask.overlap(lettucetable_mask, (lettucetable_rect.x - Player1_rect.x, lettucetable_rect.y- Player1_rect.y)):
            if player1_inv == 'None':
                player1_inv = 'Lettuce'
        if Player1_mask.overlap(buntable_mask, (buntable_rect.x - Player1_rect.x, buntable_rect.y- Player1_rect.y)):
            if player1_inv == 'None':
                player1_inv = 'Bun'
        #Dough
        if Player1_mask.overlap(dough_mask, (doughtable_rect.x - Player1_rect.x, doughtable_rect.y- Player1_rect.y)):
            if player1_inv == 'None':
                player1_inv = 'Dough'
        if Player1_mask.overlap(sauce_mask, (saucetable_rect.x - Player1_rect.x, saucetable_rect.y- Player1_rect.y)):
            if player1_inv == 'Dough':
                player1_inv = 'Raw Pizza'
        if Player1_mask.overlap(trash_mask, (trash_rect.x - Player1_rect.x, trash_rect.y- Player1_rect.y)):
            player1_inv = 'None'
            FoodWasted += 1
        
        #Cheese table
        if Player1_mask.overlap(cheesetable_mask, (cheesetable_rect.x - Player1_rect.x, cheesetable_rect.y- Player1_rect.y)):
            if player1_inv == 'Raw Pizza':
                player1_inv = 'Raw Cheese Pizza'
                

        #Cutting Station
        if Player1_mask.overlap(cuttingtable_mask, (cuttingtable_rect.x - Player1_rect.x, cuttingtable_rect.y- Player1_rect.y)):
            if player1_inv == 'Cooked Burger':
                player1_inv = 'Chopped Beef'
        if Player1_mask.overlap(cuttingtable_mask, (cuttingtable_rect.x - Player1_rect.x, cuttingtable_rect.y- Player1_rect.y)):
            if player1_inv == 'Potato':
                player1_inv = 'Raw Fries'

        #Soda
        if Player1_mask.overlap(RedSoda_mask, (RedSoda_rect.x - Player1_rect.x, RedSoda_rect.y- Player1_rect.y+20)):
            if player1_inv == 'None':
                player1_inv = 'Red Soda'
        if Player1_mask.overlap(BlueSoda_mask, (BlueSoda_rect.x - Player1_rect.x, BlueSoda_rect.y- Player1_rect.y+20)):
            if player1_inv == 'None':
                player1_inv = 'Blue Soda'
        if Player1_mask.overlap(TealSoda_mask, (TealSoda_rect.x - Player1_rect.x, TealSoda_rect.y- Player1_rect.y+20)):
            if player1_inv == 'None':
                player1_inv = 'Teal Soda'
        if Player1_mask.overlap(PinkSoda_mask, (PinkSoda_rect.x - Player1_rect.x, PinkSoda_rect.y- Player1_rect.y+20)):
            if player1_inv == 'None':
                player1_inv = 'Pink Soda'
        
        #Chopped Beef holder
        if Player1_mask.overlap(ChoppedBeeftable_mask, (ChoppedBeeftable_rect.x+20 - Player1_rect.x, ChoppedBeeftable_rect.y- Player1_rect.y)):
            if player1_inv == 'Chopped Beef':
                player1_inv = 'None'
                ChoppedBeefAmount += 3 
            if player1_inv == 'Cheese Pizza' and ChoppedBeefAmount > 0:
                player1_inv = 'Beef Pizza'
                ChoppedBeefAmount -= 1
        #Potato
        if Player1_mask.overlap(potatotable_mask, (potatotable_rect.x - Player1_rect.x, potatotable_rect.y- Player1_rect.y+20)):
            if player1_inv == 'None':
                player1_inv = 'Potato'
                

    P1item_surf = P1item[P1invID]        
    P1item_surf = pygame.transform.scale(P1item_surf, (130,130))
    P1item2_surf = P1item2[P1inv2ID]        
    P1item2_surf = pygame.transform.scale(P1item2_surf, (70,70))
    P2item_surf = P2item[P2invID]        
    P2item_surf = pygame.transform.scale(P2item_surf, (130,130))
    P2item2_surf = P2item2[P2inv2ID]        
    P2item2_surf = pygame.transform.scale(P2item2_surf, (70,70))
    

    if Stove1Timer !=0:
        
        Stove1Timer -= 0.1
        StoveAnimation = 1
    if Stove1Timer < 0:
        StoveAnimation = 0
        Stove1Timer = 0
        if stove1Slot == 'Raw Burger':
            stove1Slot = 'Cooked Burger'
        if stove1Slot == 'Raw Cheese Pizza':
            stove1Slot = 'Cheese Pizza'

    if Stove2Timer !=0:
        
        Stove2Timer -= 0.1
        Stove2Animation = 1
    if Stove2Timer < 0:
        Stove2Animation = 0
        Stove2Timer = 0
        if stove2Slot == 'Raw Burger':
            stove2Slot = 'Cooked Burger'
        if stove2Slot == 'Raw Cheese Pizza':
            stove2Slot = 'Cheese Pizza'
    
    if fryer1Timer !=0:
        
        fryer1Timer -= 0.1
        fryerAnimation = 1
    if fryer1Timer < 0:
        fryer1Animation = 0
        fryer1Timer = 0
        if fryer1Slot == 'Raw Fries':
            fryer1Slot = 'Fries'
    


    if NPC1_order_buffer <= 0:
        if NPC1_order == 0:
            NPC1_order = random.randint(1,3)
            NPC1_order_buffer = 0
    elif NPC1_order_buffer > 0:
        NPC1_order_buffer -= 0.1

    if NPC1_order == 0:
        NPC1_ticket_surf = NPC1_ticket_sprites[0]
    elif NPC1_order == 1:
        NPC1_ticket_surf = NPC1_ticket_sprites[1]
    elif NPC1_order == 2:
        NPC1_ticket_surf = NPC1_ticket_sprites[2]
    elif NPC1_order == 3:
        NPC1_ticket_surf = NPC1_ticket_sprites[3]
    
    if NPC2_order_buffer <= 0:
        if NPC2_order == 0:
            NPC2_order = random.randint(1,3)
            NPC2_order_buffer = 0
    elif NPC2_order_buffer > 0:
        NPC2_order_buffer -= 0.1

    if NPC2_order == 0:
        NPC2_ticket_surf = NPC2_ticket_sprites[0]
    elif NPC2_order == 1:
        NPC2_ticket_surf = NPC2_ticket_sprites[1]
    elif NPC2_order == 2:
        NPC2_ticket_surf = NPC2_ticket_sprites[2]
    elif NPC2_order == 3:
        NPC2_ticket_surf = NPC2_ticket_sprites[3]
    
    if NPC3_order_buffer <= 0:
        if NPC3_order == 0:
            NPC3_order = random.randint(1,1)
            NPC3_order_buffer = 0
    elif NPC3_order_buffer > 0:
        NPC3_order_buffer -= 0.1
    

    if NPC3_order == 0:
        NPC3_ticket_surf = NPC3_ticket_sprites[0]
    elif NPC3_order == 1:
        NPC3_ticket_surf = NPC3_ticket_sprites[1]
    elif NPC3_order == 2:
        NPC3_ticket_surf = NPC3_ticket_sprites[2]
    elif NPC3_order == 3:
        NPC3_ticket_surf = NPC3_ticket_sprites[3]
    elif NPC3_order == 4:
        NPC3_ticket_surf = NPC3_ticket_sprites[4]
    
    if NPC4_order_buffer <= 0:
        if NPC4_order == 0:
            NPC4_order = random.randint(1,6)
            NPC4_order_buffer = 0
    elif NPC4_order_buffer > 0:
        NPC4_order_buffer -= 0.1
    

    if NPC4_order == 0:
        NPC4_ticket_surf = NPC4_ticket_sprites[0]
    elif NPC4_order == 1:
        NPC4_ticket_surf = NPC4_ticket_sprites[1]
    elif NPC4_order == 2:
        NPC4_ticket_surf = NPC4_ticket_sprites[2]
    elif NPC4_order == 3:
        NPC4_ticket_surf = NPC4_ticket_sprites[3]
    elif NPC4_order == 4:
        NPC4_ticket_surf = NPC4_ticket_sprites[4]
    elif NPC4_order == 5:
        NPC4_ticket_surf = NPC4_ticket_sprites[5]
    elif NPC4_order == 6:
        NPC4_ticket_surf = NPC4_ticket_sprites[6]

    if NPC5_order_buffer <= 0:
        if NPC5_order == 0:
            if random.randint(1, 100) >= 30:
                NPC5_order = random.randint(1,3)
            else:
                NPC5_order = random.randint(4,7)
            NPC5_order_buffer = 0
    elif NPC5_order_buffer > 0:
        NPC5_order_buffer -= 0.1
    

    if NPC5_order == 0:
        NPC5_ticket_surf = NPC5_ticket_sprites[0]
    elif NPC5_order == 1:
        NPC5_ticket_surf = NPC5_ticket_sprites[1]
    elif NPC5_order == 2:
        NPC5_ticket_surf = NPC5_ticket_sprites[2]
    elif NPC5_order == 3:
        NPC5_ticket_surf = NPC5_ticket_sprites[3]
    elif NPC5_order == 4:
        NPC5_ticket_surf = NPC5_ticket_sprites[4]
    elif NPC5_order == 5:
        NPC5_ticket_surf = NPC5_ticket_sprites[5]
    elif NPC5_order == 6:
        NPC5_ticket_surf = NPC5_ticket_sprites[6]
    elif NPC5_order == 7:
        NPC5_ticket_surf = NPC5_ticket_sprites[7]

    
    
    #NPC4_ticket_sprites = [Nothing, Ticket_BPS, Ticket_BP, Ticket_CP, Ticket_S, Ticket_PL, Ticket_2PL]



    keys = pygame.key.get_pressed()
    #Player 2 Controls
    if keys [pygame.K_RIGHT]:
        Player2_rect.x += 2
        if Player2_mask.overlap(Player1_mask, (Player1_rect.x - Player2_rect.x, Player1_rect.y - Player2_rect.y)):
            Player2_rect.x -= 2
        right2="Y"
    else:
        right2="N"
    if keys [pygame.K_LEFT]:
        Player2_rect.x -= 2
        if Player2_mask.overlap(Player1_mask, (Player1_rect.x - Player2_rect.x, Player1_rect.y - Player2_rect.y)):
            Player2_rect.x += 2
        left2="Y"
    else:
        left2="N"
    if keys [pygame.K_UP]:
        Player2_rect.y -= 2
        if Player2_mask.overlap(Player1_mask, (Player1_rect.x - Player2_rect.x, Player1_rect.y - Player2_rect.y)):
            Player2_rect.y += 2
        up2="Y"
    else:
        up2="N"
    if keys [pygame.K_DOWN]:
        Player2_rect.y += 2
        if Player2_mask.overlap(Player1_mask, (Player1_rect.x - Player2_rect.x, Player1_rect.y - Player2_rect.y)):
            Player2_rect.y -= 2
        down2="Y"
    else:
        down2="N"
   
    if keys [pygame.K_SLASH]: #PLAYER 2 INTERATION KEY
        #NPC 1
        if Player2_mask.overlap(NPC1_mask, (NPC1_rect.x - Player2_rect.x, NPC1_rect.y - Player2_rect.y)):
            if player2_inv == 'P&L' and NPC1_order == 1: #[Nothing, Ticket_PL, Ticket_2PL, Ticket_D]
                player2_inv = 'None'
                Score += 5 + random.randint(1,3)
                NPC1_order = 0
                NPC1_order_buffer = 120
            if player2_inv == '2P&L' and NPC1_order == 2:
                player2_inv = 'None'
                Score += 7 + random.randint (2, 4)
                NPC1_order = 0
                NPC1_order_buffer = 120
            if player2_inv == '2P' and NPC1_order == 3:
                player2_inv = 'None'
                Score += 6 + random.randint(2,3)
                NPC1_order = 0
                NPC1_order_buffer = 120
                FoodMade += 1
        #NPC 2
        if Player2_mask.overlap(NPC2_mask, (NPC2_rect.x - Player2_rect.x, NPC2_rect.y - Player2_rect.y)):
            if player2_inv == 'P&L' and NPC2_order == 1: #[Nothing, Ticket_PL, Ticket_2PL, Ticket_D]
                player2_inv = 'None'
                Score += 5 + random.randint(1,3)
                NPC2_order = 0
                NPC2_order_buffer = 120
                FoodMade +=1
            if player2_inv == '2P&L' and NPC2_order == 2:
                player2_inv = 'None'
                Score += 7 + random.randint (2, 4)
                NPC2_order = 0
                NPC2_order_buffer = 120
                FoodMade +=1
            if player2_inv == '2P' and NPC2_order == 3:
                player2_inv = 'None'
                Score += 6 + random.randint(2,3)
                NPC2_order = 0
                NPC2_order_buffer = 120
                FoodMade +=1
        
        #NPC 3
        if Player2_mask.overlap(NPC3_mask, (NPC3_rect.x - Player2_rect.x, NPC3_rect.y - Player2_rect.y)):
            if player2_inv == 'Beef Pizza' and NPC3_order == 1:
                player2_inv = 'None'
                NPC3_order = 4
            if player2_inv == 'Beef Pizza' and NPC3_order == 2:
                player2_inv = 'None'
                NPC3_order = 0
                NPC3_order_buffer = 200
                Score += 20 + random.randint(2,5)
                FoodMade +=1
            if player2_inv == 'Blue Soda' and NPC3_order == 4:
                player2_inv = 'None'
                NPC3_order = 0
                NPC3_order_buffer = 200
                Score += 20 + random.randint(2,5)
                FoodMade +=1
            if player2_inv == 'Blue Soda' and NPC3_order == 1:
                player2_inv = 'None'
                NPC3_order = 2
        
        #NPC 4
        if Player2_mask.overlap(NPC4_mask, (NPC4_rect.x - Player2_rect.x, NPC4_rect.y - Player2_rect.y)):
            if player2_inv == 'Beef Pizza' and NPC4_order == 1:
                player2_inv = 'None'
                NPC4_order = 4
            if player2_inv == 'Blue Soda' and NPC4_order == 1:
                player2_inv = 'None'
                NPC4_order = 2
            if player2_inv == 'Beef Pizza' and NPC4_order == 2:
                player2_inv = 'None'
                NPC4_order = 0
                NPC4_order_buffer = 150
                Score += 25 + random.randint(1,4)
                FoodMade +=1
            if player2_inv == 'Cheese Pizza' and NPC4_order == 3:
                player2_inv = 'None'
                NPC4_order = 0
                NPC4_order_buffer = 150
                Score += 25 + random.randint(1,4)
                FoodMade +=1
            if player2_inv == 'Blue Soda' and NPC4_order == 4:
                player2_inv = 'None'
                NPC4_order = 0
                NPC4_order_buffer = 150
                Score += 25 + random.randint(1,4)
                FoodMade +=1
            if player2_inv == 'P&L' and NPC4_order == 5:
                player2_inv = 'None'
                NPC4_order = 0
                NPC4_order_buffer = 150
                Score += 15 + random.randint(1,4)
                FoodMade +=1
            if player2_inv == '2P&L' and NPC4_order == 6:
                player2_inv = 'None'
                NPC4_order = 0
                NPC4_order_buffer = 150
                Score += 20 + random.randint(1,4)
                FoodMade +=1
        
        #NPC 5 [Nothing, Ticket_PLF, Ticket_F, Ticket_PL, Ticket_S, Ticket_RS, Ticket_TS, Ticket_PS]
        if Player2_mask.overlap(NPC5_mask, (NPC5_rect.x - Player2_rect.x, NPC5_rect.y - Player2_rect.y)):
            if player2_inv == 'P&L' and NPC5_order == 1:
                player2_inv = 'None'
                NPC5_order = 2
            if player2_inv == 'Fries' and NPC5_order == 2:
                player2_inv = 'None'
                NPC5_order = 0
                NPC5_order_buffer = 100
                Score += 15 + random.randint(1,10)
                FoodMade += 1
            if player2_inv == 'P&L' and NPC5_order == 3:
                player2_inv = 'None'
                NPC5_order = 0
                NPC5_order_buffer = 100
                Score += 15 + random.randint(1,10)
                FoodMade += 1
            if player2_inv == 'Fries' and NPC5_order == 1:
                player2_inv = 'None'
                NPC5_order = 3
            if player2_inv == 'Blue Soda' and NPC5_order == 4:
                player2_inv = 'None'
                NPC5_order = 0
                NPC5_order_buffer = 20
                Score += 3 + random.randint(1,2)
                FoodMade += 1
            if player2_inv == 'Red Soda' and NPC5_order == 5:
                player2_inv = 'None'
                NPC5_order = 0
                NPC5_order_buffer = 20
                Score += 3 + random.randint(1,2)
                FoodMade += 1
            if player2_inv == 'Teal Soda' and NPC5_order == 6:
                player2_inv = 'None'
                NPC5_order = 0
                NPC5_order_buffer = 20
                Score += 3 + random.randint(1,2)
                FoodMade += 1
            if player2_inv == 'Pink Soda' and NPC5_order == 7:
                player2_inv = 'None'
                NPC5_order = 0
                NPC5_order_buffer = 20
                Score += 3 + random.randint(1,2)
                FoodMade += 1
            
            
            
        #BurgerMakingStation
        if Player2_mask.overlap(BMS_mask, (BMS_rect.x - Player2_rect.x, BMS_rect.y- Player2_rect.y)):
            if BMS_Stand == [] and player2_inv == 'Bun':
                BMS_Stand.append('Bun')
                BMS_surf = BMS_sprites[1]
                player2_inv = 'None'
            elif BMS_Stand == ['Bun'] and player2_inv == 'Cooked Burger':
                BMS_Stand.append('Patty')
                BMS_surf = BMS_sprites[2]
                player2_inv = 'None'
            #Bun Patty Route
            elif BMS_Stand == ['Bun', 'Patty'] and player2_inv == 'Cooked Burger':
                BMS_Stand.append('Patty') #2 Patties
                BMS_surf = BMS_sprites[5]
                player2_inv = 'None'
            elif BMS_Stand == ['Bun', 'Patty'] and player2_inv == 'Lettuce':
                BMS_Stand.append('Lettuce')
                BMS_surf = BMS_sprites[3]
                player2_inv = 'None'
            #Bun Patty Lettuce Bun
            elif BMS_Stand == ['Bun', 'Patty', 'Lettuce'] and player2_inv == 'Bun':
                BMS_Stand.append('Bun')
                BMS_surf = BMS_sprites[4]
                player2_inv = 'None'
            #Bun Patty2
            elif BMS_Stand == ['Bun', 'Patty', 'Patty'] and player2_inv == 'Bun':
                BMS_Stand.append('Bun')
                BMS_surf = BMS_sprites[6]
                player2_inv = 'None'
            elif BMS_Stand == ['Bun', 'Patty', 'Patty'] and player2_inv == 'Lettuce':
                BMS_Stand.append('Lettuce')
                BMS_surf = BMS_sprites[7]
                player2_inv = 'None'
            elif BMS_Stand == ['Bun', 'Patty', 'Patty', 'Lettuce'] and player2_inv == 'Bun':
                BMS_Stand.append('Bun')
                BMS_surf = BMS_sprites[8]
                player2_inv = 'None'
            elif BMS_Stand == ['Bun', 'Patty', 'Patty', 'Bun']:
                BMS_Stand.clear()
                BMS_surf = BMS_sprites[0]
                player2_inv = '2P'
            elif BMS_Stand == ['Bun', 'Patty', 'Patty', 'Lettuce', 'Bun']:
                BMS_Stand.clear()
                BMS_surf = BMS_sprites[0]
                player2_inv = '2P&L'
            elif BMS_Stand == ['Bun', 'Patty', 'Lettuce', 'Bun']:
                BMS_Stand.clear()
                BMS_surf = BMS_sprites[0]
                player2_inv = 'P&L'


        if Player2_mask.overlap(stove_mask, (stove_rect.x - Player2_rect.x, stove_rect.y- Player2_rect.y)):
            if player2_inv == 'Raw Burger' and stove1Slot == 'None':
                Stove1Timer = 30
                stove1Slot = 'Raw Burger'
                player2_inv = 'None'
            elif player2_inv == 'None' and stove1Slot == 'Cooked Burger':
                player2_inv = 'Cooked Burger'
                stove1Slot = 'None'

            if player2_inv == 'Raw Cheese Pizza' and stove1Slot == 'None':
                Stove1Timer = 70
                stove1Slot = 'Raw Cheese Pizza'
                player2_inv = 'None'
            elif player2_inv == 'None' and stove1Slot == 'Cheese Pizza':
                player2_inv = 'Cheese Pizza'
                stove1Slot = 'None'
        #Stove2        
        if Player2_mask.overlap(stove2_mask, (stove2_rect.x - Player2_rect.x, stove2_rect.y- Player2_rect.y)):
            if player2_inv == 'Raw Burger' and stove2Slot == 'None':
                Stove2Timer = 30
                stove2Slot = 'Raw Burger'
                player2_inv = 'None'
            elif player2_inv == 'None' and stove2Slot == 'Cooked Burger':
                player2_inv = 'Cooked Burger'
                stove2Slot = 'None'
        
            if player2_inv == 'Raw Cheese Pizza' and stove2Slot == 'None':
                Stove2Timer = 70
                stove2Slot = 'Raw Cheese Pizza'
                player2_inv = 'None'
            elif player2_inv == 'None' and stove2Slot == 'Cheese Pizza':
                player2_inv = 'Cheese Pizza'
                stove2Slot = 'None'


        #Beef table
        if Player2_mask.overlap(beeftable_mask, (beeftable_rect.x - Player2_rect.x, beeftable_rect.y- Player2_rect.y)):
            if player2_inv == 'None':
                player2_inv = 'Raw Burger'
        if Player2_mask.overlap(lettucetable_mask, (lettucetable_rect.x - Player2_rect.x, lettucetable_rect.y- Player2_rect.y)):
            if player2_inv == 'None':
                player2_inv = 'Lettuce'
        if Player2_mask.overlap(buntable_mask, (buntable_rect.x - Player2_rect.x, buntable_rect.y- Player2_rect.y)):
            if player2_inv == 'None':
                player2_inv = 'Bun'
        if Player2_mask.overlap(dough_mask, (doughtable_rect.x - Player2_rect.x, doughtable_rect.y- Player2_rect.y)):
            if player2_inv == 'None':
                player2_inv = 'Dough'
        if Player2_mask.overlap(sauce_mask, (saucetable_rect.x - Player2_rect.x, saucetable_rect.y- Player2_rect.y)):
            if player2_inv == 'Dough':
                player2_inv = 'Raw Pizza'
        if Player2_mask.overlap(trash_mask, (trash_rect.x - Player2_rect.x, trash_rect.y- Player2_rect.y)):
            player2_inv = 'None'
            FoodWasted += 1
        
        #Cheese table
        if Player2_mask.overlap(cheesetable_mask, (cheesetable_rect.x - Player2_rect.x, cheesetable_rect.y- Player2_rect.y)):
            if player2_inv == 'Raw Pizza':
                player2_inv = 'Raw Cheese Pizza'

        #Cutting Station
        if Player2_mask.overlap(cuttingtable_mask, (cuttingtable_rect.x - Player2_rect.x, cuttingtable_rect.y- Player2_rect.y)):
            if player2_inv == 'Cooked Burger':
                player2_inv = 'Chopped Beef'
        if Player2_mask.overlap(cuttingtable_mask, (cuttingtable_rect.x - Player2_rect.x, cuttingtable_rect.y- Player2_rect.y)):
            if player2_inv == 'Potato':
                player2_inv = 'Raw Fries'
            
        #Frier
        if Player2_mask.overlap(fryer_mask, (fryer_rect.x - Player2_rect.x, fryer_rect.y- Player2_rect.y)):
            if player2_inv == 'Raw Fries' and fryer1Slot == 'None':
                fryer1Timer = 40
                fryer1Slot = 'Raw Fries'
                player2_inv = 'None'
        if Player2_mask.overlap(fryer_mask, (fryer_rect.x - Player2_rect.x, fryer_rect.y- Player2_rect.y)):
            if player2_inv == 'None' and fryer1Slot == 'Fries':
                fryer1Slot = 'None'
                player2_inv = 'Fries'
            
        #Potato
        if Player2_mask.overlap(potatotable_mask, (potatotable_rect.x - Player2_rect.x, potatotable_rect.y- Player2_rect.y+20)):
            if player2_inv == 'None':
                player2_inv = 'Potato'

        #Sodas
        if Player2_mask.overlap(RedSoda_mask, (RedSoda_rect.x - Player2_rect.x, RedSoda_rect.y- Player2_rect.y+20)):
            if player2_inv == 'None':
                player2_inv = 'Red Soda'
        if Player2_mask.overlap(BlueSoda_mask, (BlueSoda_rect.x - Player2_rect.x, BlueSoda_rect.y- Player2_rect.y+20)):
            if player2_inv == 'None':
                player2_inv = 'Blue Soda'
        if Player2_mask.overlap(TealSoda_mask, (TealSoda_rect.x - Player2_rect.x, TealSoda_rect.y- Player2_rect.y+20)):
            if player2_inv == 'None':
                player2_inv = 'Teal Soda'
        if Player2_mask.overlap(PinkSoda_mask, (PinkSoda_rect.x - Player2_rect.x, PinkSoda_rect.y- Player2_rect.y+20)):
            if player2_inv == 'None':
                player2_inv = 'Pink Soda'
        
        #Chopped Beef holder
        if Player2_mask.overlap(ChoppedBeeftable_mask, (ChoppedBeeftable_rect.x - Player2_rect.x, ChoppedBeeftable_rect.y- Player2_rect.y)):
            if player2_inv == 'Chopped Beef':
                player2_inv = 'None'
                ChoppedBeefAmount += 1
            if player2_inv == 'Cheese Pizza' and ChoppedBeefAmount > 0:
                    player2_inv = 'Beef Pizza'
                    ChoppedBeefAmount -= 1
        

    if NPC2MoveTime > 0:
        NPC2MoveTime -= 1
    else:
        NPC2_Direct = random.randint(1, 10)#1, 9
        NPC2MoveTime = random.randint(10, 40)

    if NPCMoveTime > 0:
        NPCMoveTime -= 1
    else:
        NPC1_Direct = random.randint(1, 6)#1, 9
        NPCMoveTime = random.randint(10, 100)

    if NPC3MoveTime > 0:
        NPC3MoveTime -= 1
    else:
        NPC3_Direct = random.randint(1, 6)#1, 9
        NPC3MoveTime = random.randint(10, 100)
    
    if NPC4MoveTime > 0:
        NPC4MoveTime -= 1
    else:
        NPC4_Direct = random.randint(1, 6)#1, 9
        NPC4MoveTime = random.randint(10, 100)

    if NPC5MoveTime > 0:
        NPC5MoveTime -= 1
    else:
        NPC5_Direct = random.randint(1, 6)#1, 9
        NPC5MoveTime = random.randint(10, 100)
    
    
    NPC1_index += 0.1
    NPC2_index += 0.1
    NPC3_index += 0.1
    NPC4_index += 0.1
    NPC5_index += 0.1


    if 1 == 1:#NPC1
        if NPC1_index >= 2:
            NPC1_index = 0
        if NPC1_Direct == 1:
            if NPC1_index > 1:
                NPC1_surf = Dino_NPC_sprites[7]
                NPC1_surf = pygame.transform.flip(NPC1_surf, 180, 0)
            if NPC1_index < 1:
                NPC1_surf = Dino_NPC_sprites[6]
                NPC1_surf = pygame.transform.flip(NPC1_surf, 180, 0)
        if NPC1_Direct == 2:
            if NPC1_index > 1:
                NPC1_surf = Dino_NPC_sprites[7]
            if NPC1_index < 1:
                NPC1_surf = Dino_NPC_sprites[6]
        if NPC1_Direct == 3:
            if NPC1_index > 1:
                NPC1_surf = Dino_NPC_sprites[2]
            if NPC1_index < 1:
                NPC1_surf = Dino_NPC_sprites[3]
        if NPC1_Direct == 4:
            if NPC1_index > 1:
                NPC1_surf = Dino_NPC_sprites[4]
            if NPC1_index < 1:
                NPC1_surf = Dino_NPC_sprites[5]
        if NPC1_Direct > 4:
            if NPC1_index > 1:
                NPC1_surf = Dino_NPC_sprites[0]
            if NPC1_index < 1:
                NPC1_surf = Dino_NPC_sprites[1]
            
        if 1 == 1:#NPC2
            if NPC2_index >= 2:
                NPC2_index = 0
            if NPC2_Direct == 1:
                if NPC2_index > 1:
                    NPC2_surf = Patch_NPC_sprites[7]
                    NPC2_surf = pygame.transform.flip(NPC2_surf, 180, 0)
                if NPC2_index < 1:
                    NPC2_surf = Patch_NPC_sprites[6]
                    NPC2_surf = pygame.transform.flip(NPC2_surf, 180, 0)
            if NPC2_Direct == 2:
                if NPC2_index > 1:
                    NPC2_surf = Patch_NPC_sprites[7]
                if NPC2_index < 1:
                    NPC2_surf = Patch_NPC_sprites[6]
            if NPC2_Direct == 3:
                if NPC2_index > 1:
                    NPC2_surf = Patch_NPC_sprites[2]
                if NPC2_index < 1:
                    NPC2_surf = Patch_NPC_sprites[3]
            if NPC2_Direct == 4:
                if NPC2_index > 1:
                    NPC2_surf = Patch_NPC_sprites[4]
                if NPC2_index < 1:
                    NPC2_surf = Patch_NPC_sprites[5]
            if NPC2_Direct > 4:
                if NPC2_index > 1:
                    NPC2_surf = Patch_NPC_sprites[0]
                if NPC2_index < 1:
                    NPC2_surf = Patch_NPC_sprites[1]         
    
        if 1 == 1:#NPC3
            if NPC3_index >= 2:
                NPC3_index = 0
            if NPC3_Direct == 1:
                if NPC3_index > 1:
                    NPC3_surf = Jason_NPC_sprites[7]
                    NPC3_surf = pygame.transform.flip(NPC3_surf, 180, 0)
                if NPC3_index < 1:
                    NPC3_surf = Jason_NPC_sprites[6]
                    NPC3_surf = pygame.transform.flip(NPC3_surf, 180, 0)
            if NPC3_Direct == 2:
                if NPC3_index > 1:
                    NPC3_surf = Jason_NPC_sprites[7]
                if NPC3_index < 1:
                    NPC3_surf = Jason_NPC_sprites[6]
            if NPC3_Direct == 3:
                if NPC3_index > 1:
                    NPC3_surf = Jason_NPC_sprites[2]
                if NPC3_index < 1:
                    NPC3_surf = Jason_NPC_sprites[3]
            if NPC3_Direct == 4:
                if NPC3_index > 1:
                    NPC3_surf = Jason_NPC_sprites[4]
                if NPC3_index < 1:
                    NPC3_surf = Jason_NPC_sprites[5]
            if NPC3_Direct > 4:
                if NPC3_index > 1:
                    NPC3_surf = Jason_NPC_sprites[0]
                if NPC3_index < 1:
                    NPC3_surf = Jason_NPC_sprites[1]          

        if 1 == 1:#NPC4
            if NPC4_index >= 2:
                NPC4_index = 0
            if NPC4_Direct == 1:
                if NPC4_index > 1:
                    NPC4_surf = Cryptid_NPC_sprites[7]
                    NPC4_surf = pygame.transform.flip(NPC4_surf, 180, 0)
                if NPC4_index < 1:
                    NPC4_surf = Cryptid_NPC_sprites[6]
                    NPC4_surf = pygame.transform.flip(NPC4_surf, 180, 0)
            if NPC4_Direct == 2:
                if NPC4_index > 1:
                    NPC4_surf = Cryptid_NPC_sprites[7]
                if NPC4_index < 1:
                    NPC4_surf = Cryptid_NPC_sprites[6]
            if NPC4_Direct == 3:
                if NPC4_index > 1:
                    NPC4_surf = Cryptid_NPC_sprites[2]
                if NPC4_index < 1:
                    NPC4_surf = Cryptid_NPC_sprites[3]
            if NPC4_Direct == 4:
                if NPC4_index > 1:
                    NPC4_surf = Cryptid_NPC_sprites[4]
                if NPC4_index < 1:
                    NPC4_surf = Cryptid_NPC_sprites[5]
            if NPC4_Direct > 4:
                if NPC4_index > 1:
                    NPC4_surf = Cryptid_NPC_sprites[0]
                if NPC4_index < 1:
                    NPC4_surf = Cryptid_NPC_sprites[1]          
        if 1 == 1:#NPC5
            if NPC5_index >= 2:
                NPC5_index = 0
            if NPC5_Direct == 1:
                if NPC5_index > 1:
                    NPC5_surf = Chiaki_NPC_sprites[7]
                    NPC5_surf = pygame.transform.flip(NPC5_surf, 180, 0)
                if NPC5_index < 1:
                    NPC5_surf = Chiaki_NPC_sprites[6]
                    NPC5_surf = pygame.transform.flip(NPC5_surf, 180, 0)
            if NPC5_Direct == 2:
                if NPC5_index > 1:
                    NPC5_surf = Chiaki_NPC_sprites[7]
                if NPC5_index < 1:
                    NPC5_surf = Chiaki_NPC_sprites[6]
            if NPC5_Direct == 3:
                if NPC5_index > 1:
                    NPC5_surf = Chiaki_NPC_sprites[2]
                if NPC5_index < 1:
                    NPC5_surf = Chiaki_NPC_sprites[3]
            if NPC5_Direct == 4:
                if NPC5_index > 1:
                    NPC5_surf = Chiaki_NPC_sprites[4]
                if NPC5_index < 1:
                    NPC5_surf = Chiaki_NPC_sprites[5]
            if NPC5_Direct > 4:
                if NPC5_index > 1:
                    NPC5_surf = Chiaki_NPC_sprites[0]
                if NPC5_index < 1:
                    NPC5_surf = Chiaki_NPC_sprites[1] 

    #[Dino_Stand, Dino_Stand2, Dino_Down, Dino_Down2, Dino_Up, Dino_Up2,
    #             Dino_LR, Dino_LR2,NPC_Empty]
#NPC1_surf = Dino_NPC_sprites[NPC1_index]

    if NPC1_Direct == 1:
        NPC1_rect.x += 2
    elif NPC1_Direct == 2:
        NPC1_rect.x -=2
    elif NPC1_Direct == 3:
        NPC1_rect.y +=2
    elif NPC1_Direct == 4:
        NPC1_rect.y -=2
    else:
        NPC1_rect.x += 0
    
    if NPC2_Direct == 1:
        NPC2_rect.x += 0.7
    elif NPC2_Direct == 2:
        NPC2_rect.x -= 0.7
    elif NPC2_Direct == 3:
        NPC2_rect.y +=0.7
    elif NPC2_Direct == 4:
        NPC2_rect.y -=0.7
    else:
        NPC2_rect.x += 0
    
    if NPC3_Direct == 1:
        NPC3_rect.x += 1
    elif NPC3_Direct == 2:
        NPC3_rect.x -= 1
    elif NPC3_Direct == 3:
        NPC3_rect.y += 1
    elif NPC3_Direct == 4:
        NPC3_rect.y -= 1
    else:
        NPC3_rect.x += 0
    
    if NPC4_Direct == 1:
        NPC4_rect.x += 1
    elif NPC4_Direct == 2:
        NPC4_rect.x -= 1
    elif NPC4_Direct == 3:
        NPC4_rect.y +=1
    elif NPC4_Direct == 4:
        NPC4_rect.y -=1
    else:
        NPC4_rect.x += 0

    if NPC5_Direct == 1:
        NPC5_rect.x += 0.8
    elif NPC5_Direct == 2:
        NPC5_rect.x -= 0.8
    elif NPC5_Direct == 3:
        NPC5_rect.y +=0.8
    elif NPC5_Direct == 4:
        NPC5_rect.y -=0.8
    else:
        NPC5_rect.x += 0
  

    


    if player1_inv == 'None':
        P1invID = 0
    elif player1_inv == 'Raw Burger':
        P1invID = 1
    elif player1_inv == 'Cooked Burger':
        P1invID = 2
    elif player1_inv == 'Lettuce':
        P1invID = 3
    elif player1_inv == 'Bun':
        P1invID = 4
    elif player1_inv == '2P':
        P1invID = 5
    elif player1_inv == '2P&L':
        P1invID = 6
    elif player1_inv == 'P&L':
        P1invID = 7
    elif player1_inv == 'Dough':
        P1invID = 8
    elif player1_inv == 'Chopped Beef':
        P1invID = 9
    elif player1_inv == 'Sauce':
        P1invID = 10
    elif player1_inv == 'Red Soda':
        P1invID = 11
    elif player1_inv == 'Blue Soda':
        P1invID = 12
    elif player1_inv == 'Teal Soda':
        P1invID = 13
    elif player1_inv == 'Pink Soda':
        P1invID = 14
    elif player1_inv == 'Raw Pizza':
        P1invID = 15
    elif player1_inv == 'Raw Cheese Pizza':
        P1invID = 16
    elif player1_inv == 'Cheese Pizza':
        P1invID = 17
    elif player1_inv == 'Beef Pizza':
        P1invID = 18
    elif player1_inv == 'Potato':
        P1invID = 21
    elif player1_inv == 'Raw Fries':
        P1invID = 22
    elif player1_inv == 'Fries':
        P1invID = 23
    
    
    if player1_inv2 == 'None':
        P1inv2ID = 0
    elif player1_inv2 == 'Raw Burger':
        P1inv2ID = 1
    elif player1_inv2 == 'Cooked Burger':
        P1inv2ID = 2
    elif player1_inv2 == 'Lettuce':
        P1inv2ID = 3
    elif player1_inv2 == 'Bun':
        P1inv2ID = 4
    elif player1_inv2 == '2P':
        P1inv2ID = 5
    elif player1_inv2 == '2P&L':
        P1inv2ID = 6
    elif player1_inv2 == 'P&L':
        P1inv2ID = 7
    elif player1_inv2 == 'Dough':
        P1inv2ID = 8
    elif player1_inv2 == 'Chopped Beef':
        P1inv2ID = 9
    elif player1_inv2 == 'Sauce':
          P1inv2ID = 10
    elif player1_inv2 == 'Red Soda':
        P1inv2ID = 11
    elif player1_inv2 == 'Blue Soda':
        P1inv2ID = 12
    elif player1_inv2 == 'Teal Soda':
        P1inv2ID = 13
    elif player1_inv2 == 'Pink Soda':
        P1inv2ID = 14
    elif player1_inv2 == 'Raw Pizza':
        P1inv2ID = 15
    elif player1_inv2 == 'Raw Cheese Pizza':
        P1inv2ID = 16
    elif player1_inv2 == 'Cheese Pizza':
        P1inv2ID = 17
    elif player1_inv2 == 'Beef Pizza':
        P1inv2ID = 18
    elif player1_inv2 == 'Potato':
        P1inv2ID = 21
    elif player1_inv2 == 'Raw Fries':
        P1inv2ID = 22
    elif player1_inv2 == 'Fries':
        P1inv2ID = 23

    
    
    
    #[P1items_nothing, P1items_RawBurger, P1items_CookedBurger, P1items_Lettuce, P1items_Bun, 
    #      P1items_P2, P1items_P2L, P1items_PL, P1items_Dough, P1items_Chopped_Beef, P1items_Sauce, 
    #      P1items_RedSoda, P1items_BlueSoda, P1items_TealSoda, P1items_PinkSoda, P1items_RP,
    #       P1items_RCP, P1items_CP, P1items_CPB, P1items_CPP, P1items_CPBP]

    
    if player2_inv == 'None':
        P2invID = 0
    elif player2_inv == 'Raw Burger':
        P2invID = 1
    elif player2_inv == 'Cooked Burger':
        P2invID = 2
    elif player2_inv == 'Lettuce':
        P2invID = 3
    elif player2_inv == 'Bun':
        P2invID = 4
    elif player2_inv == '2P':
        P2invID = 5
    elif player2_inv == '2P&L':
        P2invID = 6
    elif player2_inv == 'P&L':
        P2invID = 7
    elif player2_inv == 'Dough':
        P2invID = 8
    elif player2_inv == 'Chopped Beef':
        P2invID = 9 
    elif player2_inv == 'Sauce':
        P2invID = 10
    elif player2_inv == 'Red Soda':
        P2invID = 11
    elif player2_inv == 'Blue Soda':
        P2invID = 12
    elif player2_inv == 'Teal Soda':
        P2invID = 13
    elif player2_inv == 'Pink Soda':
        P2invID = 14
    elif player2_inv == 'Raw Pizza':
        P2invID = 15
    elif player2_inv == 'Raw Cheese Pizza':
        P2invID = 16
    elif player2_inv == 'Cheese Pizza':
        P2invID = 17
    elif player2_inv == 'Beef Pizza':
        P2invID = 18
    elif player2_inv == 'Potato':
        P2invID = 21
    elif player2_inv == 'Raw Fries':
        P2invID = 22
    elif player2_inv == 'Fries':
        P2invID = 23
    
    if player2_inv2 == 'None':
        P2inv2ID = 0
    elif player2_inv2 == 'Raw Burger':
        P2inv2ID = 1
    elif player2_inv2 == 'Cooked Burger':
        P2inv2ID = 2
    elif player2_inv2 == 'Lettuce':
        P2inv2ID = 3
    elif player2_inv2 == 'Bun':
        P2inv2ID = 4
    elif player2_inv2 == '2P':
        P2inv2ID = 5
    elif player2_inv2 == '2P&L':
        P2inv2ID = 6
    elif player2_inv2 == 'P&L':
        P2inv2ID = 7
    elif player2_inv2 == 'Dough':
        P2inv2ID = 8
    elif player2_inv2 == 'Chopped Beef':
        P2inv2ID = 9 
    elif player2_inv2 == 'Sauce':
        P2inv2ID = 10
    elif player2_inv2 == 'Red Soda':
        P2inv2ID = 11
    elif player2_inv2 == 'Blue Soda':
        P2inv2ID = 12
    elif player2_inv2 == 'Teal Soda':
        P2inv2ID = 13
    elif player2_inv2 == 'Pink Soda':
        P2inv2ID = 14
    elif player2_inv2 == 'Raw Pizza':
        P2inv2ID = 15
    elif player2_inv2 == 'Raw Cheese Pizza':
        P2inv2ID = 16
    elif player2_inv2 == 'Cheese Pizza':
        P2inv2ID = 17
    elif player2_inv2 == 'Beef Pizza':
        P2inv2ID = 18
    elif player2_inv2 == 'Potato':
        P2inv2ID = 21
    elif player2_inv2 == 'Raw Fries':
        P2inv2ID = 22
    elif player2_inv2 == 'Fries':
        P2inv2ID = 23

    #if Stove1Timer == 0 and stove1Slot == 'None':
            #StoveTimerStage = 15

    if stove1Slot == 'None':
        stove1_VT_surf = stove1_VT_sprites[15]

    if stove1Slot == 'Raw Burger':
        if round(Stove1Timer) == 30:
            stove1_VT_surf = stove1_VT_sprites[0]
        elif round(Stove1Timer) == 28:
            stove1_VT_surf = stove1_VT_sprites[1]
        elif round(Stove1Timer) == 26:
            stove1_VT_surf = stove1_VT_sprites[2]
        elif round(Stove1Timer) == 24:
            stove1_VT_surf = stove1_VT_sprites[3]
        elif round(Stove1Timer) == 22:
            stove1_VT_surf = stove1_VT_sprites[4]
        elif round(Stove1Timer) == 20:
            stove1_VT_surf = stove1_VT_sprites[5]
        elif round(Stove1Timer) == 18:
            stove1_VT_surf = stove1_VT_sprites[6]
        elif round(Stove1Timer) == 16:
            stove1_VT_surf = stove1_VT_sprites[7]
        elif round(Stove1Timer) == 14:
            stove1_VT_surf = stove1_VT_sprites[8]
        elif round(Stove1Timer) == 12:
            stove1_VT_surf = stove1_VT_sprites[9]
        elif round(Stove1Timer) == 10:
            stove1_VT_surf = stove1_VT_sprites[10]
        elif round(Stove1Timer) == 8:
            stove1_VT_surf = stove1_VT_sprites[11]
        elif round(Stove1Timer) == 6:
            stove1_VT_surf = stove1_VT_sprites[11]
        elif round(Stove1Timer) == 4:
            stove1_VT_surf = stove1_VT_sprites[13]
        elif round(Stove1Timer) == 2:
            stove1_VT_surf = stove1_VT_sprites[14]
        elif round(Stove1Timer) == 0 and stove1Slot == 'Cooked Burger':
            stove1_VT_surf = stove1_VT_sprites[14]
    
    if stove1Slot == 'Raw Cheese Pizza':
        if round(Stove1Timer) == 70:
            stove1_VT_surf = stove1_VT_sprites[0]
        if round(Stove1Timer) == 65:
            stove1_VT_surf = stove1_VT_sprites[1]
        if round(Stove1Timer) == 60:
            stove1_VT_surf = stove1_VT_sprites[2]
        if round(Stove1Timer) == 50:
            stove1_VT_surf = stove1_VT_sprites[3]
        if round(Stove1Timer) == 50:
            stove1_VT_surf = stove1_VT_sprites[4]
        if round(Stove1Timer) == 45:
            stove1_VT_surf = stove1_VT_sprites[5]
        if round(Stove1Timer) == 40:
            stove1_VT_surf = stove1_VT_sprites[6]
        if round(Stove1Timer) == 35:
            stove1_VT_surf = stove1_VT_sprites[7]
        if round(Stove1Timer) == 30:
            stove1_VT_surf = stove1_VT_sprites[8]
        if round(Stove1Timer) == 25:
            stove1_VT_surf = stove1_VT_sprites[9]
        if round(Stove1Timer) == 20:
            stove1_VT_surf = stove1_VT_sprites[10]
        if round(Stove1Timer) == 15:
            stove1_VT_surf = stove1_VT_sprites[11]
        if round(Stove1Timer) == 10:
            stove1_VT_surf = stove1_VT_sprites[12]
        if round(Stove1Timer) == 5:
            stove1_VT_surf = stove1_VT_sprites[14]
        elif round(Stove1Timer) == 0 and stove1Slot == 'Cheese Pizza':
            stove1_VT_surf = stove1_VT_sprites[14]   
    if stove2Slot == 'None':
        stove2_VT_surf = stove2_VT_sprites[15]

    if stove2Slot == 'Raw Burger':
        if round(Stove2Timer) == 30:
            stove2_VT_surf = stove2_VT_sprites[0]
        elif round(Stove2Timer) == 28:
            stove2_VT_surf = stove2_VT_sprites[1]
        elif round(Stove2Timer) == 26:
            stove2_VT_surf = stove2_VT_sprites[2]
        elif round(Stove2Timer) == 24:
            stove2_VT_surf = stove2_VT_sprites[3]
        elif round(Stove2Timer) == 22:
            stove2_VT_surf = stove2_VT_sprites[4]
        elif round(Stove2Timer) == 20:
            stove2_VT_surf = stove2_VT_sprites[5]
        elif round(Stove2Timer) == 18:
            stove2_VT_surf = stove2_VT_sprites[6]
        elif round(Stove2Timer) == 16:
            stove2_VT_surf = stove2_VT_sprites[7]
        elif round(Stove2Timer) == 14:
            stove2_VT_surf = stove2_VT_sprites[8]
        elif round(Stove2Timer) == 12:
            stove2_VT_surf = stove2_VT_sprites[9]
        elif round(Stove2Timer) == 10:
            stove2_VT_surf = stove2_VT_sprites[10]
        elif round(Stove2Timer) == 8:
            stove2_VT_surf = stove2_VT_sprites[11]
        elif round(Stove2Timer) == 6:
            stove2_VT_surf = stove2_VT_sprites[12]
        elif round(Stove2Timer) == 4:
            stove2_VT_surf = stove2_VT_sprites[13]
        elif round(Stove2Timer) == 2:
            stove2_VT_surf = stove2_VT_sprites[14]
        elif round(Stove2Timer) == 0 and stove2Slot == 'Cooked Burger':
            stove2_VT_surf = stove2_VT_sprites[14]
        
    if stove2Slot == 'Raw Cheese Pizza':
        if round(Stove2Timer) == 70:
            stove2_VT_surf = stove2_VT_sprites[0]
        if round(Stove2Timer) == 65:
            stove2_VT_surf = stove2_VT_sprites[1]
        if round(Stove2Timer) == 60:
            stove2_VT_surf = stove2_VT_sprites[2]
        if round(Stove2Timer) == 50:
            stove2_VT_surf = stove2_VT_sprites[3]
        if round(Stove2Timer) == 50:
            stove2_VT_surf = stove2_VT_sprites[4]
        if round(Stove2Timer) == 45:
            stove2_VT_surf = stove2_VT_sprites[5]
        if round(Stove2Timer) == 40:
            stove2_VT_surf = stove2_VT_sprites[6]
        if round(Stove2Timer) == 35:
            stove2_VT_surf = stove2_VT_sprites[7]
        if round(Stove2Timer) == 30:
            stove2_VT_surf = stove2_VT_sprites[8]
        if round(Stove2Timer) == 25:
            stove2_VT_surf = stove2_VT_sprites[9]
        if round(Stove2Timer) == 20:
            stove2_VT_surf = stove2_VT_sprites[10]
        if round(Stove2Timer) == 15:
            stove2_VT_surf = stove2_VT_sprites[11]
        if round(Stove2Timer) == 10:
            stove2_VT_surf = stove2_VT_sprites[12]
        if round(Stove2Timer) == 5:
            stove2_VT_surf = stove2_VT_sprites[14]
        elif round(Stove2Timer) == 0 and stove2Slot == 'Cheese Pizza':
            stove2_VT_surf = stove2_VT_sprites[14]   


    if fryer1Slot == 'None':
        fryer1_VT_surf = fryer1_VT_sprites[15]
    
    if fryer1Slot == 'Raw Fries':
        if round(fryer1Timer) == 40:
            fryer1_VT_surf = fryer1_VT_sprites[0]
        elif round(fryer1Timer) == 30:
            fryer1_VT_surf = fryer1_VT_sprites[1]
        elif round(fryer1Timer) == 28:
            fryer1_VT_surf = fryer1_VT_sprites[2]
        elif round(fryer1Timer) == 26:
            fryer1_VT_surf = fryer1_VT_sprites[3]
        elif round(fryer1Timer) == 24:
            fryer1_VT_surf = fryer1_VT_sprites[4]
        elif round(fryer1Timer) == 22:
            fryer1_VT_surf = fryer1_VT_sprites[5]
        elif round(fryer1Timer) == 20:
            fryer1_VT_surf = fryer1_VT_sprites[6]
        elif round(fryer1Timer) == 18:
            fryer1_VT_surf = fryer1_VT_sprites[7]
        elif round(fryer1Timer) == 16:
            fryer1_VT_surf = fryer1_VT_sprites[8]
        elif round(fryer1Timer) == 14:
            fryer1_VT_surf = fryer1_VT_sprites[9]
        elif round(fryer1Timer) == 12:
            fryer1_VT_surf = fryer1_VT_sprites[10]
        elif round(fryer1Timer) == 10:
            fryer1_VT_surf = fryer1_VT_sprites[11]
        elif round(fryer1Timer) == 8:
            fryer1_VT_surf = fryer1_VT_sprites[12]
        elif round(fryer1Timer) == 6:
            fryer1_VT_surf = fryer1_VT_sprites[13]
        elif round(fryer1Timer) == 4:
            fryer1_VT_surf = fryer1_VT_sprites[14]
        elif round(fryer1Timer) == 0 and fryer1Slot == 'Fries':
            fryer1_VT_surf = fryer1_VT_sprites[14]


    StoveTimerStage = 5
    fryerTimerStage = 5

    if ChoppedBeefAmount > 0:
        ChoppedBeeftable_surf = ChoppedBeeftable_sprites[0]
        ChoppedBeeftable_surf = pygame.transform.scale(ChoppedBeeftable_surf,(200,200))
    else:
        ChoppedBeeftable_surf = ChoppedBeeftable_sprites[1]
        ChoppedBeeftable_surf = pygame.transform.scale(ChoppedBeeftable_surf,(200,200))

    if player1inv_buffer != 0:
        player1inv_buffer -= 0.1
    if player1inv_buffer < 0:
        player1inv_buffer = 0
    
    if player2inv_buffer != 0:
        player2inv_buffer -= 0.1
    if player2inv_buffer < 0:
        player2inv_buffer = 0
    
    if keys [pygame.K_q]:
        if player1inv_buffer == 0:
            player1inv_subparty = player1_inv
            player1_inv = player1_inv2
            player1_inv2 = player1inv_subparty
            player1inv_buffer = 2
    
    if keys [pygame.K_PERIOD]:
        if player2inv_buffer == 0:
            player2inv_subparty = player2_inv
            player2_inv = player2_inv2
            player2_inv2 = player2inv_subparty
            player2inv_buffer = 2

    print(player2_inv2)

    
    
    
    screen.blit(ground_surf, (0, 0))
    screen.blit(stove_surf,(stove_rect))
    screen.blit(stove2_surf,(stove2_rect))

    
    

    
    

    screen.blit(beeftable_surf,(beeftable_rect))
    screen.blit(lettucetable_surf,(lettucetable_rect))
    screen.blit(cheesetable_surf,(cheesetable_rect))
    screen.blit(buntable_surf,(buntable_rect))
    screen.blit(doughtable_surf,(doughtable_rect))
    screen.blit(saucetable_surf,(saucetable_rect))
    screen.blit(cuttingtable_surf,(cuttingtable_rect))
    screen.blit(potatotable_surf,(potatotable_rect))
    screen.blit(trash_surf,(trash_rect))
    screen.blit(fryer_surf,(fryer_rect))
    fryer_surf = pygame.transform.scale(fryer_surf,(200,200))
    screen.blit(BMS_surf,(BMS_rect))

    screen.blit(BlueSoda, (BlueSoda_rect))
    screen.blit(RedSoda, (RedSoda_rect))
    screen.blit(TealSoda, (TealSoda_rect))

    screen.blit(PinkSoda, (PinkSoda_rect))
    
    screen.blit(ChoppedBeeftable_surf, (ChoppedBeeftable_rect))
    
    BMS_surf = pygame.transform.scale(BMS_surf,(150,150))
    screen.blit(P1item_surf,(P1inv_rect))
    screen.blit(P2item_surf,(P2inv_rect))
    player_animation()
    #Environment_Collision()
    screen.blit(NPC1_surf, (NPC1_rect))
    screen.blit(NPC2_surf, (NPC2_rect))
    screen.blit(NPC3_surf, (NPC3_rect))
    screen.blit(NPC4_surf, (NPC4_rect))
    screen.blit(NPC5_surf, (NPC5_rect))
    screen.blit(Player1_surf,(Player1_rect))
    screen.blit(Player2_surf,(Player2_rect))
    screen.blit(P1item_surf, (P1items_rect))
    

    if Player2_mask.overlap(NPC1_mask, (NPC1_rect.x - Player2_rect.x, NPC1_rect.y - Player2_rect.y)):
        screen.blit(NPC1_ticket_surf, (NPC1_ticket_rect))
    elif Player1_mask.overlap(NPC1_mask, (NPC1_rect.x - Player1_rect.x, NPC1_rect.y - Player1_rect.y)):
        screen.blit(NPC1_ticket_surf, (NPC1_ticket_rect))

    if Player2_mask.overlap(NPC2_mask, (NPC2_rect.x - Player2_rect.x, NPC2_rect.y - Player2_rect.y)):
        screen.blit(NPC2_ticket_surf, (NPC2_ticket_rect))
    elif Player1_mask.overlap(NPC2_mask, (NPC2_rect.x - Player1_rect.x, NPC2_rect.y - Player1_rect.y)):
        screen.blit(NPC2_ticket_surf, (NPC2_ticket_rect))

    if Player2_mask.overlap(NPC3_mask, (NPC3_rect.x - Player2_rect.x, NPC3_rect.y - Player2_rect.y)):
        screen.blit(NPC3_ticket_surf, (NPC3_ticket_rect))
    elif Player1_mask.overlap(NPC3_mask, (NPC3_rect.x - Player1_rect.x, NPC3_rect.y - Player1_rect.y)):
        screen.blit(NPC3_ticket_surf, (NPC3_ticket_rect))
    
    if Player2_mask.overlap(NPC4_mask, (NPC4_rect.x - Player2_rect.x, NPC4_rect.y - Player2_rect.y)):
        screen.blit(NPC4_ticket_surf, (NPC4_ticket_rect))
    elif Player1_mask.overlap(NPC4_mask, (NPC4_rect.x - Player1_rect.x, NPC4_rect.y - Player1_rect.y)):
        screen.blit(NPC4_ticket_surf, (NPC4_ticket_rect))
    
    if Player2_mask.overlap(NPC5_mask, (NPC5_rect.x - Player2_rect.x, NPC5_rect.y - Player2_rect.y)):
        screen.blit(NPC5_ticket_surf, (NPC5_ticket_rect))
    elif Player1_mask.overlap(NPC5_mask, (NPC5_rect.x - Player1_rect.x, NPC5_rect.y - Player1_rect.y)):
        screen.blit(NPC5_ticket_surf, (NPC5_ticket_rect))
    
    
    #Player1_surf = pygame.transform.scale(Player1_surf, PlayerImgSize)
    #Player2_surf = pygame.transform.scale(Player2_surf, PlayerImgSize)
    screen.blit(stove1_VT_surf,(stove1_VT_rect))
    screen.blit(stove2_VT_surf,(stove2_VT_rect))
    screen.blit(fryer1_VT_surf,(fryer1_VT_rect))
    screen.blit(P1inv, (P1inv_rect))
    screen.blit(P2inv, (P2inv_rect))

    screen.blit(P1item2_surf, (P1items2_rect))
    screen.blit(P2item2_surf, (P2items2_rect))
    screen.blit(P1inv2, (P1inv2_rect))
    screen.blit(P2inv2, (P2inv2_rect))
    
    

    text_surface = test_font.render('Money: $' + str(Score), False, 'white')
    text2_surface = test_font.render('Time: ' + str(round(Time)), False, 'white')
    screen.blit(text_surface,(5,320))
    screen.blit(text2_surface,(5,360))

    
    

    if Time <= 0:
        Overtime = FoodMade * 2
        FinalScore = Score + round(FoodMade/2) + round(OverTime/3) - FoodWasted
        #FinalScore = 500 Score tester
        screen.blit(EndScreenTicket, (50,50))
        EndScreenTicket = pygame.transform.scale(EndScreenTicket,(700,700))
        EndScreenMoney = test_font2.render('$' + str(Score), False, 'Black')
        screen.blit(EndScreenMoney,(365,210))
        EndScreenFoodMade = test_font2.render(str(FoodMade), False, 'Black')
        screen.blit(EndScreenFoodMade,(440,265))
        EndScreenOverTime = test_font2.render(str(OverTime), False, 'Black')
        screen.blit(EndScreenOverTime,(410,325))
        EndScreenFoodWasted = test_font2.render(str(FoodWasted), False, 'Black')
        screen.blit(EndScreenFoodWasted, (500,385))
        EndScreenFinalScore = test_font2.render(str(FinalScore), False, 'Black')
        screen.blit(EndScreenFinalScore, (180,600))
        if FinalScore >= 0 and FinalScore <= 50:
            EndScreenText = "Oh..."
            EndScreenText2 = "Thats bad..."
            EndScreenText3 = ""
        elif FinalScore >= 51 and FinalScore <= 100:
            EndScreenText = "Eh..."
            EndScreenText2 = "That'll work'"
            EndScreenText3 = ""
        elif FinalScore >= 101 and FinalScore <= 150:
            EndScreenText = "Oh!"
            EndScreenText2 = "Good grief..."
            EndScreenText3 = ""
        elif FinalScore >= 151 and FinalScore <= 200:
            EndScreenText = "Cool"
            EndScreenText2 = "Your good"
            EndScreenText3 = "at this."
        elif FinalScore >= 201 and FinalScore <= 250:
            EndScreenText = "Wow!"
            EndScreenText2 = "Your an "
            EndScreenText3 = "expert huh?"
        elif FinalScore >= 251 and FinalScore <= 300:
            EndScreenText = "Good job!"
            EndScreenText2 = "Now THATS"
            EndScreenText3 = "a paycheck!"
        elif FinalScore >= 301 and FinalScore <= 350:
            EndScreenText = " Perfect!"
            EndScreenText2 = "  Really got"
            EndScreenText3 = " makin'"
        elif FinalScore >= 351 and FinalScore <= 400:
            EndScreenText = "Dang..."
            EndScreenText2 = "Teamwork for"
            EndScreenText3 = "the win..."
        elif FinalScore >= 401 and FinalScore <= 999:
            EndScreenText = "Huh..."
            EndScreenText2 = "Is this"
            EndScreenText3 = "fun for you?"
        elif FinalScore >= 1000 and FinalScore <= 4999:
            EndScreenText = "..!"
            EndScreenText2 = "Touch."
            EndScreenText3 = "Grass."
        elif FinalScore >= 5000 and FinalScore <= 9999:
            EndScreenText = "..!"
            EndScreenText2 = "So your no"
            EndScreenText3 = "hacking..?"
        elif FinalScore >= 10000 and FinalScore <= 999999:
            EndScreenText = "Once again..."
            EndScreenText2 = "Touch."
            EndScreenText3 = "Grass."
        elif FinalScore >= 1000000 and FinalScore <= 10000000:
            EndScreenText = "Your..."
            EndScreenText2 = "Joking..."
            EndScreenText3 = "Right..?"
        elif FinalScore >= 10000000:
            EndScreenText = "have fun"
            EndScreenText2 = "With taxes..."
            EndScreenText3 = "..."

            
        

        EndScreenPhrase = test_font.render(EndScreenText, False, 'Red')
        EndScreenPhrase2 = test_font.render(EndScreenText2, False, 'Red')
        EndScreenPhrase3 = test_font.render(EndScreenText3, False, 'Red')
        
        screen.blit(EndScreenPhrase, (430,200))
        screen.blit(EndScreenPhrase2, (450,230))
        screen.blit(EndScreenPhrase3, (480,260))
        OvertimeSave = open('highscoreSave.py', 'w')
        OvertimeSave.write('Latest Score' + str(FinalScore))
        OvertimeSave.close

        Time = 0
    pygame.display.update()
    clock.tick(60)