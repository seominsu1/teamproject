from django.shortcuts import render,redirect
from restaurant.forms import ResinputForm
from menu.forms import MenuinputForm
from restaurant.models import restaurant
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,'test.html')

#음식점 위치 (테스트버전)
def rest_map(request):
    return render(request,'restaurant_map.html')

#음식점 DB 넣기 (staff만 가능)
##계정 생성 후에 staff_only 코드 넣기
def rest_input(request):
    if request.method=='GET':
        print('get')
        resinputForm=ResinputForm()
        return render(request,'restaurant_register.html',{'resinputForm':resinputForm})
    elif request.method=='POST':
        print('post')
        resinputForm=ResinputForm(request.POST)

        if resinputForm.is_valid():
            print('유효함')
            resinput=resinputForm.save(commit=False)
            # resinput.writer=request.user
            resinput.save()
            return redirect('/staff/restInput')
        print('유효하지 않음')

#음식점 세부정보 사이트
def rest_detail(request,bid):
    rest=restaurant.objects.get(Q(id=bid))

    # 음식점 세부 정보+지도+메뉴 띄우는 건 get 방식(음식점id만 있으면 출력)
    if request.method=='GET':
        rest_info=ResinputForm(instance=rest)
        return render(request,'rest_detail.html',{'rest_info':rest_info})
    # 같은 화면 내에 댓글+평점 창도 있으니깐, 그때는 post
    # 기존에 생성되어있는 댓글 목록 보여져야 됨 (음식점id 외래키로 하는 review 모두 출력)
    else:
        return render(request,'test.html')

def testtest(request):
    return render(request,'testtest.html')

def rest_menu_input(request,bid):
    rest = restaurant.objects.get(Q(id=bid))
    rest_info = ResinputForm(instance=rest)
    if request.method=='GET':
        menuinputForm=MenuinputForm()
        return render(request,'menu_register.html',{'menuinputForm':menuinputForm, 'rest_info':rest_info})
    elif request.method=='POST':
        menuinputForm=MenuinputForm(request.POST)

        if menuinputForm.is_valid():
            print('유효함')
            menuinput=menuinputForm.save(commit=False)
            menuinput.restaurant_id=bid
            menuinput.save()
            return redirect('/staff/menuInput/'+str(bid))
