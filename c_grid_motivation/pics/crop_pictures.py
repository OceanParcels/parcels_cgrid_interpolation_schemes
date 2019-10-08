from os import system

def crop_file(f, size):
    system("cp pic_crop.tex tmp.tex")
    system("sed 's/XXX/%d/g' tmp.tex > tmp2.tex" % size)
    system("sed 's/YYY/%s/g' tmp2.tex > tmp3.tex" % f)
    system("pdflatex tmp3.tex")
    pdf = f[:-3] + "pdf"
    cropped_png = f[:-4] + "_cropped.png"
    system("mv tmp3.pdf %s" % pdf)
    system("convert -density 600 -quality 100 %s %s" % (pdf, cropped_png))
    system("rm tmp*")


pic_files = ['two_jets_analytical.png', 'two_jets_A.png', 'two_jets_C_no_result.png', 'two_jets_C.png']
for f in pic_files:
    crop_file(f, 4)

pic_files = ['two_jets_CWrong_no_result.png', 'two_jets_CWrong.png']
for f in pic_files:
    crop_file(f, 2)
