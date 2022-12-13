import pygame as pg
import sys
import random
def check_bound(obj_rct, scr_rct):
    
    #第一引数はこうかとんrectまたは爆弾rect
    #第二引数はスクリーンrect 
    #範囲内なら+1　範囲外なら-1
    yoko , tate = 1 ,1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko= -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko,tate
def main():
    clock = pg.time.Clock()
    
    font = pg.font.Font(None,100)#文字フォント設定
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1500,800))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()
    
    tori_sfc = pg.image.load("fig/3.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 1000,500

    tori2_sfc = pg.image.load("fig/4.png")
    tori2_sfc = pg.transform.rotozoom(tori2_sfc,0,2.0)
    tori2_rct = tori2_sfc.get_rect()
    tori2_rct.center = 500,250

    bomb_sfc = pg.Surface((60,60))#正方形のからのサーフェイス
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc,(255,0,0), (30,30),10)#整形
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0,scrn_rct.width)
    bomb_rct.centery = random.randint(0,scrn_rct.height)
    scrn_sfc.blit(bomb_sfc,bomb_rct)
    vx ,vy = 1 ,1

    while True :
        scrn_sfc.blit(pgbg_sfc,pgbg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:#ウィンドウの「ｘ」が押されたら終了
                return
        key_dic = pg.key.get_pressed()#キーが押された時の動作
        #右に表示されるこうかとん(p1)の操作
        if key_dic [pg.K_UP]:
            tori_rct.centery -= 1
        if key_dic [pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dic [pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dic [pg.K_RIGHT]:
            tori_rct.centerx += 1
        if check_bound(tori_rct, scrn_rct) != (1,1):
            if key_dic [pg.K_UP]:
                tori_rct.centery += 1
            if key_dic [pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dic [pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dic [pg.K_RIGHT]:
                tori_rct.centerx -= 1

        #左に表示されるこうかとん(p2)の操作
        if key_dic [pg.K_w]:
            tori2_rct.centery -= 1
        if key_dic [pg.K_s]:
            tori2_rct.centery += 1
        if key_dic [pg.K_a]:
            tori2_rct.centerx -= 1
        if key_dic [pg.K_d]:
            tori2_rct.centerx += 1
        if check_bound(tori2_rct, scrn_rct) != (1,1):
            if key_dic [pg.K_w]:
                tori2_rct.centery += 1
            if key_dic [pg.K_s]:
                tori2_rct.centery -= 1
            if key_dic [pg.K_a]:
                tori2_rct.centerx += 1
            if key_dic [pg.K_d]:
                tori2_rct.centerx -= 1
                
        
        scrn_sfc.blit(tori_sfc,tori_rct)
        scrn_sfc.blit(tori2_sfc,tori2_rct)
        
        bomb_rct.move_ip(vx,vy)#爆弾位置情報
        scrn_sfc.blit(bomb_sfc,bomb_rct)
        yoko,tate = check_bound(bomb_rct,scrn_rct)
        vx *= yoko
        vy *= tate

        if  tori_rct.colliderect(bomb_rct) or tori2_rct.colliderect(bomb_rct):#1p,2pが爆弾に接触すると次のwhile文に入る
            while True:
                txt = font.render("GAME OVER",True,(0,0,0))#ゲームオーバー表示
                scrn_sfc.blit(txt,(610,400))
                pg.display.update()
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:#エスケープキーを押したら終了
                        return
                    if event.type == pg.QUIT:#ウィンドウの「ｘ」が押されたら終了
                        return

        pg.display.update()
        clock.tick(1000)
    
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()