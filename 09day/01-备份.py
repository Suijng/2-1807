import pygame
import random
SCREEN_RECT=pygame.Rect(0,0,480,600)
CREATE_ENEMY_EVENT = pygame.USEREVENT
class GameSprite(pygame.sprite.Sprite):#父类
	def __init__(self,imagename,speed=1,speeds=1):
		
		super().__init__()#调用父类方法
	
		self.image = pygame.image.load(imagename)
		self.rect = self.image.get_rect()
		self.speed=speed
		self.speeds=speeds

	def update(self):
		self.rect.y+=self.speed

class EnemySprite(GameSprite):#敌机子类
	def __init__(self):
		self.imagename='./images/enemy0.png'
		super().__init__(self.imagename)

		self.speed=random.randint(1,3)#敌机初始化速度

		self.rect.bottom=0#敌机随机初始化的位置
		maxvalue=SCREEN_RECT.width-self.rect.width
		self.rect.x=random.randint(0,maxvalue)

	def update(self):
		super().update()


class BackGroundSprite(GameSprite):#背景精灵
	def __init__(self,is_alt=False):
		self.imagename='./images/background.png'
		super().__init__(self.imagename,5)
		if is_alt:
			self.rect.y=-self.rect.height

	def update(self):
		super().update()
		if self.rect.top>=SCREEN_RECT.height:
			self.rect.y=-self.rect.height
		#判断是否移除屏幕
		elif self.rect.y>=SCREEN_RECT.height:
			self.kill()#讲精灵从组中删除


class Hero(GameSprite):#英雄精灵
	def __init__(self):
		super().__init__('./images/hero.gif',0)

		self.rect.centerx=SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 30
		self.bullet_group=pygame.sprite.Group()

	def update(self):
		self.rect.x+=self.speed
		self.rect.y+=self.speeds
		if self.rect.left<0:
			self.rect.left=0
		if self.rect.right>SCREEN_RECT.right:
			self.rect.right=SCREEN_RECT.right
		if self.rect.top<0:
			self.rect.top=0
		if self.rect.bottom>SCREEN_RECT.bottom:
			self.rect.bottom=SCREEN_RECT.bottom

	def fire(self):
		bullet=BulletSprite()#创建多发子弹
		bullet.rect.centerx=self.rect.centerx
		bullet.rect.y=self.rect.top-35
		self.bullet_group.add(bullet)

		bullet1=BulletSprite()#创建多发子弹
		bullet1.rect.centerx=self.rect.centerx-36
		bullet1.rect.y=self.rect.top-2
		self.bullet_group.add(bullet1)
	
		bullet2=BulletSprite()#创建多发子弹
		bullet2.rect.centerx=self.rect.centerx+36
		bullet2.rect.y=self.rect.top-2
		self.bullet_group.add(bullet2)

class BulletSprite(GameSprite):#子弹精灵
	def __init__(self):
		self.imagename='./images/bullet2.png'
		super().__init__(self.imagename,-20)

	def update(self):
		super().update()
		if self.rect.bottom<=0:#销毁子弹
			self.kill()





	
