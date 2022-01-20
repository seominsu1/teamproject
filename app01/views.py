from django.shortcuts import render,redirect
from restaurant.forms import ResinputForm

# Create your views here.
def home(request):
    return render(request,'test.html')

#메인화면
def main_page(request):
    return render(request, 'main.html')

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

