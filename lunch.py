import random
import sys

# Windows 콘솔 인코딩 호환성 처리
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

# 점심 메뉴 목록 (카테고리별)
LUNCH_MENU = {
    "한식": [
        "김치찌개", "된장찌개", "제육볶음", "비빔밥", "순두부찌개",
        "국밥 (돼지/순대/설렁탕)", "불고기", "부대찌개", "칼국수"
    ],
    "중식": [
        "짜장면", "짬뽕", "볶음밥", "마라탕", "마파두부덮밥", "탕수육+만두 세트"
    ],
    "일식": [
        "돈까스", "라멘", "초밥", "가츠동/규동", "우동+튀김", "카레라이스"
    ],
    "양식/패스트푸드": [
        "수제버거", "파스타", "피자", "샌드위치/서브웨이", "샐러드볼"
    ],
    "분식/간편식": [
        "떡볶이+튀김", "김밥+라면", "비빔국수", "만두국"
    ]
}

def pick_lunch():
    category = random.choice(list(LUNCH_MENU.keys()))
    menu = random.choice(LUNCH_MENU[category])

    print("=" * 40)
    print("        🍱 오늘의 점심 메뉴 추천 🍱")
    print("=" * 40)
    print(f"  ▶ 분류: {category}")
    print(f"  ▶ 추천 메뉴: [ {menu} ]")
    print("=" * 40)
    print("  맛있고 든든한 점심 식사 되세요! ✨\n")

if __name__ == "__main__":
    pick_lunch()
