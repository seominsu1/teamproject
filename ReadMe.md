# Seohyun's 

-------------------------------------
<페이지 구성>
* 레스토랑 세부 정보
* 레스토랑 DB 구성
* 레스토랑별 리뷰 및 평점관리

<API 사용>
* 지도 API
* Google Analytics API
-------------------------------------


## 레스토랑 세부 정보 (rest_detail.html)
- 음식점 이름, 분류, 연락처, 영업시간 및 주소 등 세부사항 정리
- 대표 메뉴판 구성
- 사용자 리뷰창 구성

## 사용된 DB 목록
- restaurant_restaurant : 음식점 세부정보
- menu_menu : 음식점별 메뉴 데이터 (Foreign Key : restaurnat_restaurnat.id)
- restaurant_comment : 음식점별 리뷰 (Foreign Key : restaurnat_restaurnat.id)

## Google Analytics API
- 사용자별 주요 방문 사이트, 실시간 이용 정보 등을 수집
- 고객 흥미 극대화를 위한 맞춤형 전략 수립에 활용
