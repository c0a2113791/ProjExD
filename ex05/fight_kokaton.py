import pygame as pg
import os
import random
import sys


main_dir = os.path.split(os.path.abspath(__file__))[0]

#スクリーンの作成
class Screen: 
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect() 

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 

#こうかとんの表示
class Bird:
    key_delta = { #十字キーを押した際の設定
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]  
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)                    

    def Attak(self):
        return Shot(self)

#こうかとんの卵の設定
class Shot:
    def __init__(self, chr:Bird):
        self.sfc = pg.image.load("fig/pngegg.png")
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 0.1)
        self.rct = self.sfc.get_rect()
        self.rct.center = chr.rct.center

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr:Screen):
        self.rct.move_ip(0,8)
        self.blit(scr)


class Bomb:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

# 作成途中
def load_sound(file):
    """because pygame can be be compiled without mixer."""
    if not pg.mixer:
        return None

    file = os.path.join(main_dir, "data", file)
    try:
        sound = pg.mixer.Sound(file)
        return sound

    except pg.error:
        print("Warning, unable to load, %s" % file)
    return None


def main():
    if pg.get_sdl_version()[0] == 2:
        pg.mixer.pre_init(44100, 32, 2, 1024)
    pg.init()

    if pg.mixer and not pg.mixer.get_init():
        print("Warning, no sound")
        pg.mixer = None

    boom_sound = load_sound("boom.wav")
    shoot_sound = load_sound("car_door.wav")
    if pg.mixer:
        music = os.path.join(main_dir, "data", "house_lo.wav")
        pg.mixer.music.load(music)
        pg.mixer.music.play(-1)

    clock =pg.time.Clock()

    # スクリーンの描画
    scr = Screen("逃げろ！こうかとん", (1600,900), "fig/pg_bg.jpg")

    #こうかとんの描画
    kkt = Bird("fig/6.png", 2.0, (900,400))
    kkt.update(scr)

    shots = []

    #爆弾の生成
    bkd_lst = []
    color_lst = ["red", "green", "blue", "yellow", "magenta"]
    for i in range(3  ) :
        bkd = Bomb(color_lst[i%5], 10, (random.choice(range(-2, 3)), random.choice(range(-2, 3))), scr)
        bkd_lst.append(bkd)
    # bkd.update(scr)

    while True:        
        scr.blit()

        for event in pg.event.get():    #ゲームを止める際の設定
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:    #spaceを押した際に作動する
                shots.append(kkt.Attak())
                
        for i in range(len(shots)):   #生成される卵をリストに入れる
            shots[i].update(scr)
        kkt.update(scr)
        for i in range(len(bkd_lst)):
            bkd_lst[i].update(scr)
            if kkt.rct.colliderect(bkd_lst[i].rct):    #爆弾とこうかとんの当たった際の反応
                return
            
            for j in range(len(shots)):
                if bkd_lst[i].rct.colliderect(shots[j].rct):  #卵と爆弾が当たった際の反応
                    bkd_lst.remove(bkd_lst[i])   #爆弾リスト[i]番目の爆弾を消去
            

        pg.display.update()
        clock.tick(1000)
    

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()