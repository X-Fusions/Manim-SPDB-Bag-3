from os import write
from manim import *

class NamaAnggota(MovingCameraScene):
    def construct(self):
        
        #Text yang dimasukkan
        judul = Tex("Sistem Persamaan Diferensial Biasa Bagian III")
        nama_anggota = Tex("Anggota:", color='#753A88')
        first_line = Tex("Bima Fahimna (12919012)", color='#CC2B5E')
        second_line = Tex("Faza Muhammad Patradhia (12919032)", color='#CC2B5E')
        third_line = Tex("Naufal Arkhan Anan (12919022) ", color='#CC2B5E')
        final_line = Tex("Shafiyya Mulyana (12919047)", color='#CC2B5E')
        line1 = Line(LEFT*5,RIGHT*5)
        group1 = VGroup(judul,line1).arrange(DOWN)
        #color_final_line = Tex("Hope you like it too!")

        #Coloring
        #color_final_line.set_color_by_gradient(BLUE,PURPLE)
        group1.set_color_by_gradient('#CC2B5E','#753A88')

      
        #Posisi Text
        first_line.next_to(nama_anggota, DOWN)
        second_line.next_to(first_line, DOWN)
        third_line.next_to(second_line, DOWN)
        final_line.next_to(third_line, DOWN)

        #Menampilkan Text
        self.play(Write(group1.move_to(UP*1), run_time=3))
        self.wait(2)
        self.play(group1.animate.scale(1.2).shift(UP*1.1))
        self.wait(1)
        self.play(FadeInFromLarge(nama_anggota))
        self.play( Write(first_line), Write(second_line),Write(third_line), Write(final_line))
        self.wait(3)
        self.play(FadeOutAndShift(group1,direction=UP),FadeOut(nama_anggota), FadeOut(first_line), FadeOut(second_line),
                    FadeOut(third_line), FadeOut(final_line))
        self.wait(2)
        
class KonversiPDB(Scene):
    def construct(self):

        #Text
        line_1 = Tex("PDB Orde Tinggi", color='#4169E1')
        line_1_2 = Tex("PDB Orde Satu", color ='#4169E1')
        pers_orde_tinggi = Tex("$y\\textsuperscript{n} =\,$","$F$","$(t,y,y',\, ... \, ,y\\textsuperscript{n-1})$")
        line_2_2 = Tex("dimisalkan", color='#4169E1')
        line_2_3 = MathTex("y_n'=","F","(t,y_1,y_2, \, ... \, ,y_n)")
        line_2_4 = Tex("$y_1$","$=\,$","$y$")
        line_2_5 = Tex("$y_2$","$=\,$","$y'$")
        line_2_6 = Tex("$y_3$","$=\,$","$y''$")
        line_2_7 = Tex("$...$")
        line_2_8 = Tex("$y_n$","$=\,$","$y^{n-1}$")
        line_3_1 = Tex("$y_1'$","$=\,$","$y'$")
        line_3_2 = Tex("$y_2'$","$=\,$","$y_3$")
        line_3_3 = Tex("$y_3'$","$=\,$","$y_4$")
        line_3_4 = Tex("$y_{n-1}'$","$=\,$","$y_n$")

        kotak1 = Rectangle(height=6,width=9)
        kotak2 = Rectangle(height=4,width=6)
        self.add(kotak1)

        group_2_2 = VGroup(line_2_4,line_2_5,line_2_6,line_2_7,line_2_8)
     
        #Contoh penulisan equation
        #equation_example = Tex("$\\vec{X}_0 \\cdot \\vec{Y}_1 = 3$")
        
        #Posisi Text & Color
        pers_orde_tinggi.next_to(line_1,DOWN)
        pers_orde_tinggi[1].set_color('#C21E56')
        line_2_3[1].set_color('#C21E56')
        
                        
        #Menampilkan Text dan Animasi
        self.play(Write(line_1.scale(1.2), run_time=2))
        self.wait(1)
        self.play(line_1.animate.shift(UP*2).scale(1/1.2))
        self.play(Write(pers_orde_tinggi.move_to(UP*0.9)))
        self.wait(5.5)
        self.play(AddTextWordByWord(line_2_2.move_to(DOWN*0.2), run_time=5, time_per_char=0.15))

        self.play(FadeIn(group_2_2.arrange(RIGHT).next_to(line_2_2,DOWN,buff=1,aligned_edge=DOWN), run_time=1))
        self.play(ApplyMethod(line_2_4.shift,DOWN*0.0771,LEFT*0.7),ApplyMethod(line_2_5.shift,LEFT*0.4),
                    ApplyMethod(line_2_7.shift,RIGHT*0.4,DOWN*0.15),ApplyMethod(line_2_8.shift,RIGHT*0.7),run_time=0.8)
        self.play(Indicate(line_2_4), run_time = 2.5, color = '#FFF700')
        self.play(Indicate(line_2_5), run_time = 2.5, color = '#FFF700')
        self.play(Indicate(line_2_6), run_time = 2.5, color = '#FFF700')
        self.wait(1.5)
        self.play(Indicate(line_2_8), run_time = 2.5, color = '#FFF700')
        self.wait(5)

        line_3_1.move_to(line_2_4)
        self.play(TransformMatchingShapes(line_2_4,line_3_1))
        self.wait(3)
        self.play(Flash(line_2_5,line_length=0.3,flash_radius=1),run_time=3)
        self.wait(2.5)

        kopi = line_2_5[0].copy()
        ca = CurvedArrow(line_2_5[0].get_center()+UP*0.3,line_3_1[2].get_center()+UP*0.2)
        self.play(Create(ca))
        self.wait(1)
        self.play(TransformMatchingShapes(line_3_1[2],kopi.move_to(line_3_1[2])))
        self.play(Uncreate(ca))
        self.wait(5)

        line_3_2.move_to(line_2_5)
        self.play(TransformMatchingShapes(line_2_5[0],line_3_2[0]))
        self.play(TransformMatchingShapes(line_2_5[2],line_3_2[2]))
        self.wait(1)

        line_3_3.move_to(line_2_6)
        self.play(TransformMatchingShapes(line_2_6[0],line_3_3[0]))
        self.play(TransformMatchingShapes(line_2_6[2],line_3_3[2]))
        self.wait(1.5)

        line_3_4.move_to(line_2_8)
        self.play(TransformMatchingShapes(line_2_8,line_3_4))
        self.wait(3)

        framebox1 = SurroundingRectangle(group_2_2, buff=0.1)
        self.play(Create(framebox1))
        self.wait(4)

        ca1 = CurvedArrow(line_3_4[2].get_center()+RIGHT*0.2+UP*0.45,pers_orde_tinggi[2].get_center()+RIGHT+RIGHT*0.8)
        self.play(Create(ca1))
        self.wait(2)
        group_2_2.add(line_3_1,line_3_2,line_3_3,line_3_4)
        self.play(FadeOut(framebox1),FadeOut(ca1),FadeOut(pers_orde_tinggi))
        self.wait(1)
        self.play(FadeOutAndShift(line_2_2,direction=DOWN),
                    FadeOutAndShift(group_2_2,direction=DOWN),FadeOutAndShift(kopi,direction=DOWN))

        line_1_2.move_to(pers_orde_tinggi)
        
        self.wait(2)
        self.play(TransformMatchingShapes(kotak1,kotak2))
        self.play(TransformMatchingShapes(line_1,line_1_2))

        line_2_3.move_to(DOWN*0.2)
        self.play(FadeIn(line_2_3))
        self.wait(2)

        svg = SVGMobject("happiness")
        svg.move_to(DOWN*2)
        self.play(Create(svg),run_time=4)
        self.wait(3)

class PDBNonlinear(GraphScene,MovingCameraScene):
    def construct(self):

        #Text
        title = Tex("Sistem ","PDB Non-Linear ","(Analisis Dinamik)")

        line_1 = MathTex("\\frac{dx}{dt}=","ax","-","\\alpha","xy")
        line_1_1 = MathTex("\\frac{dx}{dt}=","ax","-","\\alpha","xy","=","x(a-","\\alpha","y)","=","0")
        line_1_2 = MathTex("\\frac{dx}{dt}=","0")
        line_1_3 = MathTex("\\frac{dx}{dt}=","ax","-","\\alpha","xy","=","0")
        line_1_4 = MathTex("x=0","\quad","y= \\frac{a}{\\alpha}")

        line_2 = MathTex("\\frac{dy}{dt}=","\\gamma","xy","-","cy")
        line_2_1 = MathTex("\\frac{dy}{dt}=","\\gamma","xy-cy=","y(","\\gamma","x-c)=","0")
        line_2_2 = MathTex("\\frac{dy}{dt}=","0")
        line_2_3 = MathTex("\\frac{dy}{dt}=","\\gamma","xy-cy=","0")
        line_2_4 = Tex("Saat \,","$x=0$","\, diperoleh \,","$y=0$")
        line_2_5 = Tex("Saat \,","$y= \\frac{a}{\\alpha}$","\, diperoleh \,","$x=\\frac{c}{\\gamma}$")
        line_2_6 = MathTex("(0,0)")
        line_2_7 = MathTex("(\\frac{c}{\\gamma},\\frac{a}{\\alpha})")

        #line_3_1 = 

        line_M = Tex("Model Predator-Prey")

        line_3_1 = Tex("Titik Kesetimbangan")
        line_3_2 = Tex("Jenis Kestabilan")  

        group1 = VGroup(line_1,line_2)

        #Color
        line_M.set_color_by_gradient(RED,YELLOW)
        title.set_color('#DE3163')
        line_1.set_color_by_tex("\\alpha",'#DC143C')
        line_1_1.set_color_by_tex("\\alpha",'#DC143C')
        line_1_2.set_color_by_tex("\\alpha",'#DC143C')
        line_1_3.set_color_by_tex("\\alpha",'#DC143C')

        line_2.set_color_by_tex("\\gamma",'#00FFFF')
        line_2_1.set_color_by_tex("\\gamma",'#00FFFF')
        line_2_2.set_color_by_tex("\\gamma",'#00FFFF')
        line_2_3.set_color_by_tex("\\gamma",'#00FFFF')

        #Position
        line_M.next_to(group1,UP*3.2)
        title.to_corner(LEFT+UP)


        #Lain-lain
        line_3_1.scale(0.7)
        line_3_2.scale(0.7)
        line_3_1.save_state()
        line_3_2.save_state()
        line_1_4.scale(0.8)

        #Animation
        self.add(group1.arrange(DOWN))
        self.wait(8)
        self.play(Write(line_M),run_time=2)
        self.wait(4)
        self.play(ReplacementTransform(line_M,title))
        self.wait(2)
        self.play(group1.animate.shift(LEFT*4))
        self.wait(2)
        self.play(FadeIn(line_3_1.move_to(UP*0.8)))
        self.wait(1)
        self.play(FadeIn(line_3_2.move_to(DOWN*0.3)))
        self.wait(2)
        self.play(Unwrite(line_3_1))
        self.play(Unwrite(line_3_2))
        self.play(FadeOutAndShift(group1,LEFT))

        line_3_1.restore()
        line_3_1.move_to(title[0].get_center()+RIGHT*0.9+DOWN*0.8)
        self.play(Write(line_3_1))
        self.wait(2)

        line_1_2.move_to(line_1)
        self.play(Write(line_1_2))
        self.wait(1)
        
        self.play(Write(line_2_2.move_to(line_2)))
        self.wait(2)
        self.play(FadeOut(line_2_2))
        self.wait(3)
        self.play(ReplacementTransform(line_1_2,line_1_3))
        self.wait(4)
        self.play(TransformMatchingShapes(line_1_3,line_1_1))
        self.wait(7)
        self.play(line_1_1.animate.shift(UP*0.9),FadeIn(line_1_4))
        self.wait(3.5)
        self.play(FadeOut(line_1_1),line_1_4.animate.shift(UP))
        self.wait(2)
        framebox1 = SurroundingRectangle(line_1_4[0],buff=0.1)
        framebox2 = SurroundingRectangle(line_1_4[2],buff=0.1)

        self.play(Write(line_2_2))
        self.play(ReplacementTransform(line_2_2,line_2_3))
        self.wait(2)
        self.play(TransformMatchingShapes(line_2_3,line_2_1))
        self.wait(2)
        self.play(Create(framebox1),Create(framebox2))
        self.wait(4)
        self.play(FadeIn(line_2_4.move_to(DOWN).scale(0.8)))
        self.wait(4)
        self.play(FadeIn(line_2_5.move_to(DOWN*2).scale(0.8)))
        self.wait(4)
        self.play(FadeIn(line_2_6.next_to(line_2_4)))
        self.wait(3)
        self.play(FadeIn(line_2_7.next_to(line_2_5)))
        self.wait(5)

class GrafikNullcline(GraphScene,MovingCameraScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=0,
            x_max=8,
            num_graph_anchor_points=100,
            y_min=0,
            y_max=8,
            axes_color=GREEN,
            
            **kwargs
        )
        self.function_color = RED


    def construct(self):
        self.setup_axes(animate=True)
        line_1_1 = self.get_graph(lambda x: 4,color=BLUE,x_min=0)
        line_1_2 = self.get_graph(lambda x: 0,color=RED,x_min=0)
        line_1_x1 = self.get_graph(lambda x: 8,color=BLUE,x_min=0)
        line_1_x2 = self.get_graph(lambda x: 8,color=BLUE,x_min=0)
        line_2_1 = self.get_vertical_line_to_graph(4,line_1_x1,color=RED)
        line_2_2 = self.get_vertical_line_to_graph(0,line_1_x2,color=BLUE)

        dot_1 = Dot().move_to(line_1_1.points[200])
        dot_lab = MathTex("(","\\frac{c}{\\gamma}",",","\\frac{a}{\\alpha}",")").next_to(dot_1,RIGHT+UP*0.4)
        dot_2 = Dot().move_to(line_1_2.points[0])
        dot_lab2 = MathTex("(","0",",","0",")").next_to(dot_2,RIGHT+UP*0.4)
        
        line_1_1_lab = self.get_graph_label(line_1_1, label="y= \\frac{a}{\\alpha}")
        line_1_2_lab = self.get_graph_label(line_1_2, label="y=0")
        line_2_1_lab = MathTex("x=\\frac{c}{\\gamma}").set_color(RED)
        line_2_2_lab = MathTex("x=0").set_color(BLUE)

      
        title_1 = Tex("Nullcline-","$x$").move_to(UP*3+RIGHT*0.1).set_color(BLUE)
        title_2 = Tex("Nullcline-","$y$").move_to(UP*2+RIGHT*2.5).set_color(RED)

        #Warna
        dot_lab2[1].set_color(BLUE)
        dot_lab2[3].set_color(RED)
        dot_lab[1].set_color(RED)
        dot_lab[3].set_color(BLUE)

        #Posisi
        line_2_2_lab.move_to(line_2_2.get_center()+RIGHT+UP*2.7)
        line_2_1_lab.move_to(line_2_1.get_center()+RIGHT+UP*2.7)
        
        #Animasi
        self.wait(5)
        self.play(Write(title_1))
        self.wait(4)
        self.play(Create(line_2_2),Create(line_2_2_lab))
        self.wait(1)
        self.play(Create(line_1_1),Create(line_1_1_lab))
        self.wait(2)
        self.play(FadeOut(title_1))
        self.wait(2)

        self.play(Write(title_2))
        self.wait(4)
        self.play(Create(line_1_2),Create(line_1_2_lab))
        self.wait(1)
        self.play(Create(line_2_1),Create(line_2_1_lab))
        self.wait(4)

        self.play(Create(dot_1),Create(dot_lab),Create(dot_2),Create(dot_lab2))
        self.wait(6)
        groupO_1 = VGroup(dot_1,dot_2,dot_lab,dot_lab2,line_1_2,line_1_2_lab,line_2_1,line_2_1_lab)
        self.play(FadeOut(groupO_1),FadeTransform(title_2,title_1))
        self.wait(6)

        line_3_1 = MathTex("\\frac{dx}{dt}=","ax- \\alpha xy","\\approx - \\alpha xy<0")
        line_3_2 = Tex("Nilai $y$ yang lebih besar")
        line_3_3 = MathTex("\\frac{dx}{dt}=","ax- \\alpha xy","\\approx ax>0")
        line_3_4 = Tex("Nilai $y$ yang lebih kecil")
        
        line_3_1.next_to(title_1,DOWN)
        line_3_2.next_to(line_3_1,DOWN)
        line_3_3.next_to(line_1_1,DOWN)
        line_3_4.next_to(line_3_3,DOWN)

        self.play(Write(line_3_1.scale(0.8)))
        self.wait(3)
        self.play(Write(line_3_2.scale(0.8)))
        self.wait(5)
        self.play(Write(line_3_3.scale(0.8)))
        self.wait(3)
        self.play(Write(line_3_4.scale(0.8)))
        self.wait(3)

        groupO_2 = VGroup(line_3_1,line_3_2,line_3_3,line_3_4)
        arr1 = Arrow(start=RIGHT*2.5,end=LEFT*2.5).move_to(line_1_1.get_center()+UP*1.5)
        arr2 = Arrow(start=LEFT*2.5,end=RIGHT*2.5).move_to(line_1_1.get_center()+DOWN*1.5)
        arr1.set_color(BLUE)
        arr2.set_color(BLUE)
        self.play(Create(arr1),Create(arr2),FadeOut(groupO_2))
        self.wait(3)

        groupO_3 = VGroup(line_1_1,line_1_1_lab,line_2_2,line_2_2_lab,arr1,arr2)
        groupO_1.remove(dot_lab,dot_lab2,dot_1,dot_2)

        self.play(FadeOut(groupO_3))
        self.play(FadeTransform(title_1,title_2))
        self.play(Create(groupO_1),run_time=3)
        self.wait(2)

        line_4_1 = MathTex("\\frac{dy}{dt}=","\\gamma xy- cy","\\approx \\gamma xy>0")
        line_4_2 = Tex("Nilai $x$ yang lebih besar")
        line_4_3 = MathTex("\\frac{dy}{dt}","\\approx -cy<0")
        line_4_4 = Tex("Nilai $x$ yang lebih kecil")

        line_4_1.next_to(line_2_1,RIGHT)
        line_4_2.next_to(line_4_1,DOWN)
        line_4_3.next_to(line_2_1,LEFT)
        line_4_4.next_to(line_4_3,DOWN)

        self.play(Write(line_4_1.scale(0.8)))
        self.wait(2)
        self.play(Write(line_4_2.scale(0.8)))
        self.wait(4)
        self.play(Write(line_4_3.scale(0.8)))
        self.wait(2)
        self.play(Write(line_4_4.scale(0.7)))
        self.wait(3)

        groupO_4 = VGroup(line_4_1,line_4_2,line_4_3,line_4_4)
        arr3 = Arrow(DOWN*2.6,UP*2.4).move_to(line_2_1.get_center()+RIGHT*2)
        arr4 = Arrow(UP*2.6,DOWN*2.4).move_to(line_2_1.get_center()+LEFT*2)
        arr3.set_color(RED)
        arr4.set_color(RED)
        self.play(Create(arr3),Create(arr4),FadeOut(title_2),FadeOut(groupO_4))
        self.wait(2)

        self.play(FadeOut(arr3),FadeOut(arr4),FadeOut(groupO_1))
        self.wait(3)

        groupO_3.remove(arr1,arr2)
        groupO_1.add(dot_2,dot_1)
        self.play(Create(groupO_3),Create(groupO_1),run_time=4)
        self.wait(2)

        karr1 = Arrow(UP,DOWN).move_to(line_2_1.get_center()+LEFT+UP*1.4).set_color(RED)
        karr2 = Arrow(DOWN,UP).move_to(line_2_1.get_center()+RIGHT+DOWN*1.4).set_color(RED)
        karr3 = Arrow(LEFT*2.5,RIGHT*0.5).move_to(line_1_1.get_center()+DOWN*0.8+LEFT*1.9).set_color(BLUE)
        karr4 = Arrow(RIGHT*2.5,LEFT*0.5).move_to(line_1_1.get_center()+UP*0.8+RIGHT*1.9).set_color(BLUE)
        karr5 = Arrow(karr3.points[0],karr3.points[0]+DOWN*1.5,buff=0).set_color(RED)
        karr6 = Arrow(karr1.points[0],karr1.points[0]+LEFT*2.5,buff=0).set_color(BLUE)
        karr7 = Arrow(karr2.points[0],karr2.points[0]+RIGHT*2.5,buff=0).set_color(BLUE)
        karr8 = Arrow(karr4.points[0],karr4.points[0]+UP*1.5,buff=0).set_color(RED)
        karr9 = Arrow(karr1.points[0],karr1.points[0]+DOWN*1.5+LEFT*2,buff=0).set_color(PURPLE)
        karr10 = Arrow(karr2.points[0],karr2.points[0]+UP*1.5+RIGHT*2,buff=0).set_color(PURPLE)
        karr11 = Arrow(karr3.points[0],karr3.points[0]+DOWN*1.5+RIGHT*2,buff=0).set_color(PURPLE)
        karr12 = Arrow(karr4.points[0],karr4.points[0]+UP*1.5+LEFT*2,buff=0).set_color(PURPLE)
        karr_1 = Arrow(UP*0.7,DOWN*0.7,stroke_width=4).move_to(line_2_1.get_center()+LEFT*2.5).set_color(PURPLE)
        karr_2 = Arrow(DOWN*0.7,UP*0.7,stroke_width=4).move_to(line_2_1.get_center()+RIGHT*2.5).set_color(PURPLE)
        karr_3 = Arrow(RIGHT*0.7,LEFT*0.7,stroke_width=4).move_to(line_1_1.get_center()+UP*2).set_color(PURPLE)
        karr_4 = Arrow(LEFT*0.7,RIGHT*0.7,stroke_width=4).move_to(line_1_1.get_center()+DOWN*2).set_color(PURPLE)

        groupkarr = VGroup(karr1,karr2,karr3,karr4,karr5,karr6,karr7,karr8)
        groupkarr_2 = VGroup(karr9,karr10,karr11,karr12,
                            karr_1,karr_2,karr_3,karr_4)
        self.play(Create(groupkarr),run_time=4)
        self.play(Create(groupkarr_2),run_time=4)
        self.wait(2) 

class TeoremaKestabilan1(MovingCameraScene):
    def construct(self):
        judul = Tex("Liniearisasi Sistem PDB Non-Linear")
        line_1 = Tex("Menganalisis lebih lanjut tentang kestabilan dari titik kesetimbangan sistem ", 
                        "PDB nonlinier, perlu dilakukan proses"," linierisasi sistem PDB nonlinier ",
                        "menggunakan"," matriks Jacobian.",tex_environment="justify").scale(0.8)
        line_2_1 = MathTex("\\frac{dx}{dt}=","f_1(x,y)")
        line_2_2 = MathTex("\\frac{dy}{dt}=","f_2(x,y)")
        M_Jacob = Matrix([["\\frac{\\partial f_1(x,y)}{\\partial x}","\\frac{\\partial f_1(x,y)}{\\partial y}"],
                                ["\\frac{\\partial f_2(x,y)}{\\partial x}","\\frac{\\partial f_2(x,y)}{\\partial y}"]],
                                v_buff=1.5,h_buff=2.4)
        T_Jacob = MathTex("J(x,y)=")

        line_3_1 = Tex("Teorema Kestabilan lokal(*)")
        line_3_2 = Tex("Misalkan ","$(x,y)$"," adalah titik kesetimbangan dari suatu sistem PDB nonlinier dan ",
                            "$\\lambda$"," adalah ","nilai eigen (real)"," dari ","matriks Jacobian ","$J(x,y)$",
                            ", maka:",tex_environment="justify").scale(0.8)
        line_3_3 = Tex("(i) Jika ","$\\lambda <0$",", maka titik kesetimbangannya stabil lokal").scale(0.8)
        line_3_4 = Tex("(ii) Jika ","$\\lambda >0$",", maka titik kesetimbangannya tidak stabil").scale(0.8)
        line_3_5 = Tex("(iii) Jika ","$\\lambda =0$",", maka tidak dapat ditarik kesimpulan").scale(0.8)

        Jacob = VGroup(T_Jacob,M_Jacob).arrange(RIGHT)
        group_1 = VGroup(line_2_1,line_2_2)
        

        line_1.set_color_by_tex("linierisasi",'#FFD700')
        line_1.set_color_by_tex("Jacobian",'#40E0D0')
        line_3_2.set_color_by_tex("matriks Jacobian",'#40E0D0')
        line_3_2.set_color_by_tex("eigen",'#FF69B4')

        judul.to_corner(LEFT+UP)
        line_1.move_to(UP)
        Jacob.move_to(RIGHT*2)

        b1 = Brace(Jacob)
        b1text = b1.get_text("Matriks Jacobian").set_color('#40E0D0')

        self.add(judul,line_1)
        #self.play(FadeIn(line_1))
        self.wait(13)
        self.remove(judul,line_1)
        self.wait(2)
        self.play(FadeIn(group_1.arrange(DOWN)),run_time=2)
        self.wait(2)
        self.play(group_1.animate.shift(LEFT*4))
        self.play(FadeIn(Jacob))
        self.wait(2)
        self.play(Create(b1),Create(b1text))
        self.wait(3)
        self.play(Uncreate(b1),Uncreate(b1text))
        self.play(FadeOutAndShift(group_1,direction=LEFT*2),FadeOutAndShift(Jacob,direction=RIGHT*2))
        self.wait(2)


        line_3_1.to_corner(LEFT+UP,buff=0.5)
        line_3_2.move_to(UP*2)
        line_3_3.move_to(UP)
        line_3_4.next_to(line_3_3,DOWN)
        line_3_5.next_to(line_3_4,DOWN)


        self.play(Write(line_3_1))
        self.wait(1)
        self.play(FadeInFrom(line_3_2,DOWN))
        self.wait(5)
        self.play(FadeInFrom(line_3_3,DOWN*2))
        self.wait(2)
        self.play(FadeInFrom(line_3_4,DOWN*2))
        self.wait(2)
        self.play(FadeInFrom(line_3_5,DOWN*2))
        self.wait(2)

class TeoremaKestabilan2(MovingCameraScene):
    def construct(self):
        line_1_1 = Tex("Teorema Kestabilan(**)").set_color_by_gradient('#43cea2','#185a9d')
        line_1_2 = Tex("Misalkan ","$(x,y)$"," adalah titik kesetimbangan dari suatu sistem PDB nonlinear. Jika",
                        tex_environment="justify").scale(0.8)
        line_1_3 = Tex("det ","$J(x,y)>0$"," dan trace ","$J(x,y)<0$").scale(0.8)
        line_1_4 = Tex("Maka titik kesetimbangan ","$(x,y)$"," stabil lokal",". Bila tak terpenuhi, maka ",
                        "$(x,y)$"," tidak stabil", t2w={'dan':BOLD},tex_environment="justify").scale(0.8)
        line_1_5 = Tex("*trace (","$J$",") adalah jumlah elemen diagonal utama matriks ","$J$",).scale(0.5).set_color('#FAA0A0')

        model = Tex("Model ","Predator-Prey").to_corner(LEFT+UP,buff=0.7)
        line_2 = Tex("Titik Kesetimbangan").scale(0.8)
        line_2_1 = Tex("$(0,0)$"," dan ","$(\\frac{c}{\\gamma},\\frac {a}{\\alpha})$").scale(0.7)
        line_2_2 = Tex("Matriks Jacobian").scale(0.8).set_color('#40E0D0')
        line_2_3 = MathTex("J(x,y)=")
        line_2_4 = Matrix([["a- \\alpha y","- \\alpha x"],["\\gamma y","\\gamma x-c"]],h_buff=2.7)

        line_3_1 = Tex("Analisis Titik ","$(0,0)$").scale(0.8)
        line_3_2 = MathTex("J(0,0)=")
        line_3_3 = Matrix([["a","0"],["0","-c"]],h_buff=2.7)
        line_3_4 = Tex("det(","$J- \\lambda I)=$")
        line_3_5 = Matrix([["a- \\lambda","0"],["0","-c- \\lambda"]],h_buff=2.7)
        line_3_6 = MathTex("(a- \\lambda)(-c- \\lambda)=0")
        line_3_7 = Tex("$\\lambda _1=a$"," dan ","$\\lambda_2=-c$").scale(0.8)
        b_3_1 = Brace(line_3_7,DOWN).scale(0.8)
        b_3_1_text = b_3_1.get_text("tidak stabil pelana").scale(0.8)

        line_4_1 = Tex("Analisis Titik ","$(\\frac{c}{\\gamma},\\frac{a}{\\alpha})$").scale(0.8)
        line_4_2 = MathTex("J(\\frac{c}{\\gamma},\\frac{a}{\\alpha})=")
        line_4_3 = Matrix([["0","-\\alpha \\frac{c}{\\gamma}"],["\\gamma \\frac{a}{\\alpha}","0"]],v_buff=2,h_buff=2.7)
        line_4_4 = Tex("det(","$J- \\lambda I)=$")
        line_4_5 = Matrix([["-\\lambda","-\\alpha \\frac{c}{\\gamma}"],["\\gamma \\frac{a}{\\alpha}","-\\lambda"]],v_buff=2,h_buff=2.7)
        line_4_6 = MathTex("\\lambda^2+ac=0")
        line_4_7 = MathTex("\\lambda_{1,2}=\\pm \\sqrt{ac} i").scale(0.8)
        b_4_1 = Brace(line_4_7,DOWN).scale(0.8)
        b_4_1_text = b_4_1.get_text("tidak dapat disimpulkan").scale(0.8)
        

        matrix_1 = VGroup(line_2_3,line_2_4).scale(0.8).arrange(RIGHT)
        matrix_2 = VGroup(line_3_2,line_3_3).scale(0.8).arrange(RIGHT)
        matrix_3 = VGroup(line_3_4,line_3_5,line_3_6).scale(0.8).arrange(RIGHT)
        group_1 = VGroup(line_2,line_2_1).arrange(DOWN,buff=0.5)

        matrix_4 = VGroup(line_4_2,line_4_3).scale(0.8).arrange(RIGHT)
        matrix_5 = VGroup(line_4_4,line_4_5,line_4_6).scale(0.8).arrange(RIGHT)

        line_1_4[2].set_color('#50C878')
        line_1_4[5].set_color('#F4BB44')
        model[1].set_color_by_gradient('#DC143C','#F4C430')
        #model[1].set_color('#DC143C')

        line_1_1.to_corner(LEFT+UP,buff=0.5)
        line_1_2.move_to(UP*2)
        line_1_3.next_to(line_1_2,DOWN)
        line_1_4.next_to(line_1_3,DOWN)
        line_1_5.to_corner(LEFT+DOWN,buff=0.3)

        line_2_2.move_to(UP*1.7)
        line_2.move_to(UP*1.7)
        line_2_1.move_to(UP*0.6)

        line_3_1.next_to(model,DOWN,buff=1)
        line_3_7.next_to(matrix_3,DOWN)
        b_3_1.next_to(line_3_7,DOWN,buff=0.2)
        b_3_1_text.next_to(b_3_1,DOWN,buff=0.1)

        line_4_1.move_to(line_3_1)
        line_4_7.next_to(matrix_5,DOWN)
        b_4_1.next_to(line_4_7,DOWN,buff=0.2)
        b_4_1_text.next_to(b_4_1,DOWN,buff=0.1)

        self.add(line_1_1)
        self.wait(1)
        self.play(FadeInFrom(line_1_2,DOWN),FadeInFrom(line_1_3,DOWN),FadeInFrom(line_1_4,DOWN),FadeIn(line_1_5))
        self.wait(15)
        self.remove(line_1_1,line_1_2,line_1_3,line_1_4,line_1_5)
        self.add(model)
        self.wait(2)
        self.play(Write(line_2))
        self.wait(1)
        self.play(FadeInFrom(line_2_1,DOWN))
        self.wait(4)
        self.play(FadeOutToPoint(group_1,ORIGIN))
        self.play(Write(line_2_2))
        self.wait(2)
        self.play(FadeIn(matrix_1))
        self.wait(2)

        #Analisis titik 1
        self.play(FadeIn(line_3_1),FadeOut(line_2_2))
        self.wait(2)
        self.play(TransformMatchingShapes(matrix_1,matrix_2))
        self.wait(4)
        self.play(TransformMatchingShapes(matrix_2,matrix_3))
        self.wait(2)
        self.play(FadeInFrom(line_3_7,DOWN))
        self.wait(2)
        self.play(FadeIn(b_3_1),FadeIn(b_3_1_text))
        self.wait(2)
        self.play(FadeOut(line_3_7),FadeOut(b_3_1),FadeOut(b_3_1_text))

        #Analisis titik 2
        self.play(FadeTransform(line_3_1,line_4_1))
        self.wait(2)
        self.play(TransformMatchingShapes(matrix_3,matrix_4))
        self.wait(4)
        self.play(TransformMatchingShapes(matrix_4,matrix_5))
        self.wait(2)
        self.play(FadeInFrom(line_4_7,DOWN))
        self.wait(2)
        self.play(FadeIn(b_4_1),FadeIn(b_4_1_text))
        self.wait(2)

class   LiniarisasiDariJacobian(MovingCameraScene):
    def construct(self):

        model = Tex("Model ","Predator-Prey").to_corner(LEFT+UP,buff=0.7)
        line_1 = Tex("Analisis Titik ","$(\\frac{c}{\\gamma},\\frac{a}{\\alpha})$").scale(0.8)
        line_1_1 = Tex("Bentuk Linierisasi").scale(0.8)
        line_1_2 = Matrix([["\\overline{x'}"],["\\overline{y'}"]])
        conj_1 = MathTex("=")
        line_1_3 = Matrix([["0","-\\alpha \\frac{c}{\\gamma}"],["\\gamma \\frac{a}{\\alpha}","0"]],v_buff=2,h_buff=2.7)
        line_1_4 = Matrix([["\\bar{x}"],["\\bar{y}"]])

        line_2_1 = MathTex("\\overline{x'}=-\\alpha \\frac{c}{\\gamma} \\bar{y}")
        line_2_2 = MathTex("\\overline{y'}=\\gamma \\frac{a}{\\alpha} \\bar{x}")
        line_2_3 = MathTex("\\gamma \\frac{a}{\\alpha} \, \\bar{x} \, \\overline{x'}=",
                            "-\\alpha \\frac{c}{\\gamma} \, \\bar{y} \, \\overline{y'}  ").scale(0.8)
        line_2_4 = Tex("Kedua ruas di Integrasikan!").scale(0.7)
        line_2_5 = Tex("$\\gamma \\frac{a}{\\alpha} \, \\bar{x}^2 + \\alpha \\frac{c}{\\gamma} \, \\bar{y}^2=$","konstan").scale(0.8)
        b_2_1 = Brace(line_2_5,direction=DOWN)
        b_2_1_text = b_2_1.get_text("Persamaan Ellips").scale(0.8)

        matrix_1 = VGroup(line_1_2,conj_1,line_1_3,line_1_4).scale(0.8).arrange(RIGHT)
        group_2_1 = VGroup(line_2_1,line_2_2).scale(0.8).arrange(DOWN,buff=0.5)
    
        model[1].set_color_by_gradient('#DC143C','#F4C430')

        line_1_1.move_to(UP*1.8)
        line_1.next_to(model,DOWN,buff=1)

        line_2_4.move_to(UP*1.3)
        b_2_1.next_to(line_2_5,DOWN,buff=0.2)
        b_2_1_text.next_to(b_2_1,DOWN,buff=0.1)

        self.add(model)
        self.add(line_1)
        self.play(Write(line_1_1))
        self.wait(1)
        self.play(FadeIn(matrix_1))
        self.wait(2)
        self.play(FadeOut(line_1_1))
        self.wait(1)
        self.play(TransformMatchingShapes(matrix_1,group_2_1))
        self.wait(2)
        self.play(FadeOutToPoint(group_2_1,ORIGIN),FadeInFromLarge(line_2_3))
        self.wait(2)
        self.play(Write(line_2_4))
        self.wait(1)
        self.play(Transform(line_2_3,line_2_5))
        self.wait(2)
        self.play(FadeOut(line_2_4),FadeInFrom(b_2_1,DOWN*2),FadeInFrom(b_2_1_text,DOWN*2))
        self.wait(3)

class GrafikTerakhir(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=0,
            x_max=8,
            num_graph_anchor_points=100,
            y_min=0,
            y_max=8,
            axes_color=GREEN,
            
            **kwargs
        )
        self.function_color = RED

    def construct(self):

        self.setup_axes(animate=True)
        
        line_1_1 = self.get_graph(lambda x: 4,color=BLUE,x_min=0)

        dot_1 = Dot().move_to(line_1_1.points[200])
        dot_lab = MathTex("(","\\frac{c}{\\gamma}",",","\\frac{a}{\\alpha}",")").next_to(dot_1,RIGHT+UP*0.4).scale(0.8)
        elips = Ellipse(height=3,width=5.5).move_to(dot_1)

        self.add(dot_1,dot_lab)
        self.play(Create(elips))
        self.wait(2)

class Kesimpulan(MovingCameraScene):
    def construct(self):
        
        line_1 = Tex("Pada kasus Model ","Predator-Prey"," ini terdapat 2 titik kesetimbangan, yaitu:").scale(0.8)
        line_1_1 = Tex("(i) ","$(0,0)$"," jenis kestabilan: ","tidak stabil pelana").scale(0.8)
        line_1_2 = Tex("(ii) ","$(\\frac{c}{\\gamma},\\frac{a}{\\alpha})$"," jenis kestabilan: ","stabil").scale(0.8)

        end = Tex("Terima Kasih").scale(1.5)

        line_1[1].set_color_by_gradient('#DC143C','#F4C430')
        line_1_1[3].set_color('#FF7F50')
        line_1_2[3].set_color('#50C878')
        end.set_color_by_gradient('#ffd89b','#19547b')

        line_1.move_to(UP)
        line_1_2.next_to(line_1_1,DOWN,buff=0.5)

        self.add(line_1)
        self.wait(1)
        self.play(FadeInFrom(line_1_1,DOWN*2))
        self.wait(2)
        self.play(FadeInFrom(line_1_2,DOWN*2))
        self.wait(3)
        self.play(FadeOutAndShift(line_1_1,UP),FadeOutAndShift(line_1_2,UP),FadeOutAndShift(line_1,UP))

        self.play(FadeIn(end))
        self.wait(3)
        self.play(FadeOut(end))

