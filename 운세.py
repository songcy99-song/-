import streamlit as st
import datetime
import random

# 페이지 설정
st.set_page_config(
    page_title="이승호님을 위한 오늘의 운세",
    page_icon="🔮",
    layout="centered"
)

# 제목 및 안내 문구
st.title("🔮 이승호님을 위한 오늘의 운세")
st.write("생년월일을 입력하고 오늘 이승호님에게 찾아올 종합 운세와 연애운을 확인해보세요!")

st.divider()

# 사용자 입력 받기
calendar_type = st.radio("달력 구분", ["양력", "음력"], horizontal=True)

birth_date = st.date_input(
    "생년월일 선택",
    value=datetime.date(1995, 1, 1),
    min_value=datetime.date(1920, 1, 1),
    max_value=datetime.date.today()
)

# 데이터베이스 (시드 기반 결정용)
FORTUNES = [
    {"score": 95, "title": "🎉 대길(大吉)", "desc": "뜻밖의 행운과 좋은 기회가 찾아오는 날입니다. 주저하던 일이 있다면 자신 있게 도전하세요!"},
    {"score": 85, "title": "✨ 길(吉)", "desc": "주변 사람들과의 관계가 원만해지고 도움을 받게 될 하루입니다. 따뜻한 대화를 나눠보세요."},
    {"score": 75, "title": "🌱 소길(小吉)", "desc": "소소한 기쁨과 평화로움이 가득한 날입니다. 차 한 잔의 여유를 즐기며 조용히 일상을 보내기 좋습니다."},
    {"score": 60, "title": "⚖️ 평범(平)", "desc": "큰 변화 없이 무난하게 지나가는 날입니다. 성급한 결정보다는 기존 일에 충실한 것이 좋습니다."},
    {"score": 45, "title": "⚠️ 주의(注)", "desc": "감정 조절이 필요한 하루입니다. 사소한 말실수나 충동적인 행동을 경계하는 것이 좋습니다."},
]

LOVE_FORTUNES = [
    {"score": 98, "title": "💖 설렘 가득한 날", "desc": "운명적인 만남이나 뜻밖의 호감을 받을 가능성이 높습니다. 적극적으로 마음을 표현해보세요!"},
    {"score": 80, "title": "💕 따뜻한 기류", "desc": "상대방과의 대화가 매끄럽게 이어지는 날입니다. 평소 하지 못했던 솔직한 이야기를 나누기 좋습니다."},
    {"score": 70, "title": "🌿 잔잔한 평화", "desc": "큰 변화는 없지만 안정적이고 편안한 연애운입니다. 서로의 일상을 공유하며 소소한 행복을 느껴보세요."},
    {"score": 55, "title": "💬 신중한 소통 필요", "desc": "작은 오해가 생길 수 있는 날입니다. 서운한 점이 있다면 감정적으로 대하기보다 차분히 이야기하세요."},
    {"score": 40, "title": "🌧️ 나만의 시간이 필요한 날", "desc": "연애보다는 나 자신에게 집중하는 것이 좋은 하루입니다. 혼자만의 휴식을 즐겨보세요."},
]

LUCKY_ITEMS = ["파란색 아이템", "따뜻한 커피", "노란색 액세서리", "민트향 사탕", "손수건", "초록색 소품"]
DIRECTIONS = ["동쪽", "서쪽", "남쪽", "북쪽", "동남쪽", "북서쪽"]

# 버튼 클릭 시 운세 계산 및 출력
if st.button("🔮 운세 보기", use_container_width=True):
    today = datetime.date.today()

    # 생년월일 + 오늘 날짜를 조합하여 시드 생성 (하루 동안 동일한 결과 유지)
    seed_value = int(f"{birth_date.strftime('%Y%m%d')}{today.strftime('%Y%m%d')}")
    random.seed(seed_value)

    # 결과 추출
    fortune = random.choice(FORTUNES)
    love_fortune = random.choice(LOVE_FORTUNES)
    lucky_item = random.choice(LUCKY_ITEMS)
    lucky_direction = random.choice(DIRECTIONS)
    lucky_number = random.randint(1, 99)

    st.divider()
    st.subheader(f"📅 {today.strftime('%Y년 %m월 %d일')} 이승호님의 오늘의 운세")

    # 탭으로 종합운세와 연애운 분리
    tab1, tab2 = st.tabs(["🌟 종합 운세", "💖 연애운"])

    with tab1:
        st.metric(label="오늘의 종합 운세 지수", value=f"{fortune['score']}점")
        st.success(f"### {fortune['title']}\n{fortune['desc']}")

        st.markdown("#### 🍀 오늘의 행운 포인트")
        c1, c2, c3 = st.columns(3)
        c1.metric("행운의 아이템", lucky_item)
        c2.metric("행운의 방위", lucky_direction)
        c3.metric("행운의 숫자", str(lucky_number))

    with tab2:
        st.metric(label="오늘의 연애운 지수", value=f"{love_fortune['score']}점")
        st.info(f"### {love_fortune['title']}\n{love_fortune['desc']}")

    st.caption("※ 본 운세는 하루 동안 변경되지 않으며, 재미로만 참고해주시기 바랍니다.")