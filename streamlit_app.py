import streamlit as st
import json
from PIL import Image

# ====== 성경 인물 데이터 로드 ======
@st.cache_data
def load_character_data():
    """JSON 파일에서 성경 인물 데이터를 로드"""
    with open("bible_characters.json", "r", encoding="utf-8") as f:
        return json.load(f)

# ====== 앱 페이지 설정 ======
st.set_page_config(
    page_title="성경 인물 어시스턴트",
    page_icon="📖",
    layout="wide"
)

# ====== 데이터 로드 ======
character_data = load_character_data()

# ====== 제목 및 설명 ======
st.title("📖 성경 인물 어시스턴트")
st.write("성경 속 주요 인물들에 대한 정보를 검색하고 알아보세요!")

# ====== 사이드바: 인물 선택 ======
st.sidebar.title("성경 인물 목록")
selected_character = st.sidebar.selectbox(
    "인물을 선택하세요:",
    options=list(character_data.keys()),
    index=0  # 첫 번째 인물을 기본 선택
)

# ====== 메인 화면: 선택된 인물 정보 표시 ======
if selected_character:
    # 선택된 인물 데이터 가져오기
    info = character_data[selected_character]

    # 인물 이름 및 설명 표시
    st.header(f"✨ {selected_character}")
    st.write(f"**설명:** {info['설명']}")
    st.write(f"**주요 성경 구절:** {info['주요 성경 구절']}")

    # 이미지 로드 및 표시
    img_path = f"imgs/{info['이미지']}"
    try:
        img = Image.open(img_path)
        st.image(img, caption=selected_character, use_column_width=True)
    except FileNotFoundError:
        st.warning("이미지를 찾을 수 없습니다.")

# ====== 피드백 섹션 ======
st.markdown("---")
st.subheader("💬 피드백")
feedback = st.text_area("어시스턴트에 대한 의견을 남겨주세요!")
if st.button("피드백 제출"):
    # 피드백 저장 처리 (예: 파일 저장 또는 데이터베이스 연결 가능)
    with open("feedback.txt", "a", encoding="utf-8") as f:
        f.write(f"{selected_character}: {feedback}\n")
    st.success("피드백이 제출되었습니다. 감사합니다!")
