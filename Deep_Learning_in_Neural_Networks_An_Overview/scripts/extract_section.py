import re
import os

tex_header = open('tex_header.tex').read()
tex_tail = open('tex_tail.tex').read()
tex = open('DeepLearning8Oct2014.tex').read()

#  abstract = re.findall(r'\\begin{abstract}(.*?)\\end{abstract}', tex, re.S)
#  print(abstract)

section = re.findall(r'\\section(.*?)%\\newpage', tex, re.S)
#  print(len(section))
#  print(section[0])
for section_index in range(len(section)):
    if section_index >= 0:
        section_tex = tex_header + '\\section' + section[section_index] + tex_tail
        chapter_index = section_index + 1
        chapter_dir = 'Chapter' + str(chapter_index)
        #  print(chapter_dir)
        if not os.path.isdir(chapter_dir):
            os.mkdir(chapter_dir)
        chapter_section_file = open(os.path.join(chapter_dir, chapter_dir+'.tex'), 'w')
        chapter_section_file.write(section_tex)
        chapter_section_file.close()

