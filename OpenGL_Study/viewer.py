# -*- coding: utf-8 -*-
import numpy
from numpy.linalg import norm, inv
from OpenGL.GL import glCallList, glClear, glClearColor, glColorMaterial, glCullFace, glDepthFunc, glDisable,\
                      glFlush, glGetFloatv, glLightfv, glLoadIdentity, glMatrixMode, glMultMatrixf, glPopMatrix, \
                      glPushMatrix, glTranslated, glViewport, glEnable,\
                      GL_AMBIENT_AND_DIFFUSE, GL_BACK, GL_CULL_FACE, GL_COLOR_BUFFER_BIT, GL_COLOR_MATERIAL, \
                      GL_DEPTH_BUFFER_BIT, GL_DEPTH_TEST, GL_FRONT_AND_BACK, GL_LESS, GL_LIGHT0, GL_LIGHTING, \
                      GL_MODELVIEW, GL_MODELVIEW_MATRIX, GL_POSITION, GL_PROJECTION, GL_SPOT_DIRECTION
from OpenGL.constants import GLfloat_3, GLfloat_4
from OpenGL.GLU import gluPerspective, gluUnProject
from OpenGL.GLUT import glutCreateWindow, glutDisplayFunc, glutGet, glutInit, glutInitDisplayMode, \
                        glutInitWindowSize, glutMainLoop, \
                        GLUT_SINGLE, GLUT_RGB, GLUT_WINDOW_HEIGHT, GLUT_WINDOW_WIDTH


class Viewer(object):
    def __init__(self):
        self.init_interface()       # 初始化接口，创建窗口并注册渲染函数
        self.init_opengl()          # 初始化opengl配置
        self.init_scene()           # 初始化3D场景
        self.init_interaction()     # 初始化交互操作代码

    def init_interface(self):
        """初始化窗口并注册渲染函数"""
        glutInit()
        glutInitWindowSize(640, 480)
        glutCreateWindow(b'3D Modeller')
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        '''注册窗口渲染函数'''
        glutDisplayFunc(self.render)

    def init_opengl(self):
        """ 初始化opengl的配置 """
        # 模型视图矩阵
        self.inverseModelView = numpy.identity(4)
        # 模型视图矩阵的逆矩阵
        self.modelView = numpy.identity(4)
        # 开启剔除操作效果
        glEnable(GL_CULL_FACE)
        # 背面看不到的部分剔除
        glCullFace(GL_BACK)
        # 开启深度测试
        glEnable(GL_DEPTH_TEST)
        # 测试物体是否被遮挡，遮挡部分不渲染
        glDepthFunc(GL_LESS)
        # 启用0号光源
        glEnable(GL_LIGHT0)
        # 设置光源位置
        glLightfv(GL_LIGHT0, GL_POSITION, GLfloat_4(0, 0, 1, 0))
        # 设置光源照射方向
        glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, GLfloat_3(0, 0, -1))
        # 设置材质颜色
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_COLOR_MATERIAL)
        # 设置清屏颜色
        glClearColor(0.4, 0.4, 0.4, 0)

    def init_scene(self):
        # 初始化场景
        pass

    def init_interaction(self):
        # 初始化交互操作
        pass

    def main_loop(self):
        # 程序主循环开始
        glutMainLoop()

    def render(self):
        # 每次循环调用的渲染函数
        self.init_view()        # 初始化投影矩阵
        glEnable(GL_LIGHTING)   # 启动光照
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # 清空颜色缓存和深度缓存
        # 设置模型视图矩阵，此处使用单位矩阵
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        # 渲染场景
        # self.scene.render()

        # 每次渲染后恢复光照状态
        glDisable(GL_LIGHTING)
        glPopMatrix()
        # 把数据刷新到显存上
        glFlush()

    def init_view(self):
        """初始化投影矩阵"""
        xSize, ySize = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
        # 得到屏幕宽高比
        aspect_ratio = float(xSize) / float(ySize)

        # 设置投影矩阵
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        # 设置视口，应与窗口重合
        glViewport(0, 0, xSize, ySize)
        # 设置透视，摄像机上下视野幅度70度
        # 视野范围到距离摄像机1000个单位为止。
        gluPerspective(70, aspect_ratio, 0.1, 1000.0)
        # 摄像机镜头从原点后退15个单位
        glTranslated(0, 0, -15)


if __name__ == '__main__':
    viewer = Viewer()
    viewer.main_loop()












