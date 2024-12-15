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
st.write("성경 속 주요 인물들에 대한 정보를 검색하세요!")

# ====== 검색란 ======
search_query = st.text_input("🔍 성경 인물 검색", "").strip()

# 검색 결과 처리
if search_query:
    filtered_data = {
        name: info for name, info in character_data.items() if search_query.lower() in name.lower()
    }

    if filtered_data:
        for name, info in filtered_data.items():
            st.header(f"✨ {name}")
            st.write(f"**설명:** {info['설명']}")
            st.write(f"**주요 성경 구절:** {info['주요 성경 구절']}")

            # 이미지 표시
            img_path = f"imgs/{info['이미지']}"
            try:
                img = Image.open(img_path)
                st.image(img, caption=name, use_column_width=True)
            except FileNotFoundError:
                st.warning(f"{name}의 이미지를 찾을 수 없습니다.")
    else:
        st.warning("검색 결과가 없습니다. 정확한 이름을 입력했는지 확인해주세요.")
else:
    st.info("성경 인물 이름을 입력해 검색하세요.")
