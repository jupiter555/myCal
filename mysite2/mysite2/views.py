from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):

    # #1.通过loader加载模板
    # t = loader.get_template('test.html')
    # #2.t对象转化称html字符串
    # html = t.render()
    # #3.将html return至浏览器
    # return HttpResponse(html)
    # # return HttpResponse('This is index')

    #render 方案
    dic = {'username':'zhouenlai','age':78}
    return render(request,'test.html',dic)

def test_p(request):
    #测试页面传参
    dic = {}
    dic['list'] = ['xiaohong','小明','小兰']
    dic['dict'] = {'username':'zhouenlai'}
    dic['class_obj'] = Dog()
    dic['say_hi'] = say_hi
    dic['script'] = '<script>alert(111)</script>'
    dic['number'] = 1
    return render(request,'test_p.html',dic)

class Dog:
    def say(self):
        return 'hahahaha'

def say_hi():
    return 'say:hi'

def test_if(request):
    #/test_if?x=1
    x = int(request.GET.get('x',4))
    dic = {'x' : x}
    return render(request,'test_if.html',dic)

def cal_view(request):
    #GET or POST
    if request.method == 'GET':
        return render(request,'cal.html')
    elif request.method == 'POST':
        #浏览器会用POST请求提交如下数据
        # x=x_val&op=op_val&y=y_val
        #处理数据　＋－＊／
        #text框,空提交时,浏览器会带上具体text框的name及空值一并提交到服务器
        # x = int(request.POST.get('x',100))
        x = request.POST.get('x')
        if not x:
            #错误处理 将提示信息返给浏览器
            error = 'Please give me x!!'
            dic = {'error':error}
            return render(request,'cal.html',dic)
        try:
            x = int(x)
        except Exception as e:
           print('-----x is error-----')
           print(x)
           try:
                x = int(float(x))
           except Exception as e:
               error = 'The x is must be number!!'
               dic = {'error': error}
               return render(request, 'cal.html', dic)
        #TODO 检查y值：方法同上
        op = request.POST.get('op')
        y = int(request.POST.get('y'))
        result=99999999999
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y

        return render(request,'cal.html',locals())

def test_for(request):
    lst = ['小红','小兰','小吕']

    dic = {'username':'xiaoming','age':18}
    return render(request,'test_for.html',locals())

def base_view(request):

    lst = ['哈哈','哼哼']
    return render(request,'base.html',locals())

def music_view(request):
    return render(request,'music.html')

def sports_view(request):
    return render(request,'sports.html')





def shebao_view(request):
    if request.method == 'GET':

        return render(request,'shebao.html')

    if request.method == 'POST':

        base = int(request.POST.get('base'))
        is_city = int(request.POST.get('is_city'))

        geRen_old = 0
        danWei_old = 0
        geRen_out = 0
        danWei_out = 0
        geRen_work  = 0
        danWei_work = 0
        geRen_birth = 0
        danWei_birth = 0
        geRen_help = 0
        danWei_help = 0
        geRen_gold = 0
        danWei_gold = 0
        geRen = 0
        danWei = 0
        country = 0

        if base>23118:
            base = 23118
        if base<3082:
            base = 3082
        if is_city == 1:
            geRen_out = base * 0.002
            danWei_out = base * 0.008
        else:
            geRen_out = 0
            danWei_out = base * 0.008
        geRen_old = base * 0.08
        danWei_old = base * 0.19
        geRen_work = 0
        danWei_work = base * 0.005
        geRen_birth = 0
        danWei_birth = base * 0.008
        geRen_help = base * 0.02 + 3
        danWei_help = base * 0.1
        geRen_gold = base * 0.12
        danWei_gold = base * 0.12
        geRen = geRen_old+geRen_out+geRen_work+geRen_birth+geRen_help+geRen_gold
        danWei = danWei_old+danWei_out+danWei_work+danWei_birth+danWei_help+danWei_gold
        country = geRen + danWei
        return render(request,'shebao.html',locals())






