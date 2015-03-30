
#the header is to create the top of HTML document
header='''
<!DOCTYPE html>
  <HTML>
    <head>
      <title> Alfia's notes </title>
      <link rel="stylesheet" type="text/css" href="stylesheets/style.css">
       <meta charset="utf-8"/>
    </head>
   <body>'''
ender='''
</body>'''
#this creates divisions for each lesson
def generate_lesson_HTML(lesson_title, lesson_content):
    html_text_1 = '''
<div class="lesson">
    <div class="lesson_title">
        ''' '<h2>'+ lesson_title + '</h2>'
    html_text_2 = '''
    </div>
    <div class="lesson_content">
        ''' + lesson_content
    html_text_3 = '''
	    </div>
	</div>'''

    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(lesson):
    start_location = lesson.find('Lesson')
    end_location = lesson.find('I.')
    title = lesson[start_location+7 : end_location-1]
    return title

def get_content(lesson):
    start_location = lesson.find('I.')
    content = lesson[start_location+13 :]
    return content

def get_lesson_by_number(text, lesson_number):
    counter = 0
    while counter < lesson_number:
        counter = counter + 1
        next_lesson_start = text.find('Lesson')
        next_lesson_end   = text.find('Lesson', next_lesson_start + 1)
        lesson = text[next_lesson_start:next_lesson_end]
        text = text[next_lesson_end:]
    return lesson



text_file = open('Content_text.txt')
current_text = text_file.read()


def generate_all_html(text):
    current_lesson_number = 1
    lesson = get_lesson_by_number(text, current_lesson_number)
    all_html = ''
    while lesson != '':
        title = get_title(lesson)
        content = get_content(lesson)
        lesson_html = generate_lesson_HTML(title, lesson)
        all_html = all_html + lesson_html
        current_lesson_number = current_lesson_number + 1
        lesson = get_lesson_by_number(text, current_lesson_number)
    return all_html

print generate_all_html(current_text)

def finish():
	html_done= header + generate_all_html(current_text)+ ender
	return html_done


fout = open('output.txt', 'w')
fout=fout.write(finish())
#fout=header+ (generate_all_html(current_text)
