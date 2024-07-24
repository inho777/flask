import datetime
import streamlit as st
import random
from fuzzywuzzy import process
from PIL import Image

mt_brand = {
    "GUCCI": "구찌",
    "CP Company": "CP컴퍼니",
    "IWC": "IWC",
    "Kenzo": "겐조",
    "GOYARD": "고야드",
    "Golden Goose": "골든구스",
    "GRAND SEIKO": "그랜드 세이코",
    "COMME des GARCONS": "꼼데가르송",
    "Cartier": "까르띠에",
    "Chloe": "끌로에",
    "Rolex": "롤렉스",
    "LOUIS VUITTON": "루이비통",
    "MSGM": "MSGM",
    "Novis": "노비스",
    "Neil Barrett": "닐바렛",
    "DAMIANI": "다미아니",
    "Dolce & Gabbana": "돌체앤가바나",
    "Dsquared2": "디스퀘어드2",
    "LANVIN": "랑방",
    "Loro Piana": "로로피아나",
    "LOEWE": "로에베",
    "ROGER DUBUIS": "로저드뷔",
    "Rogervivier": "로저비비에",
    "Longines": "론진",
    "BALENCIAGA": "발렌시아가",
    "Valentino": "발렌티노",
    "BALLY": "발리",
    "Balmain": "발망",
    "Burberrys": "버버리",
    "Versace": "베르사체",
    "Bottega Veneta": "보테가 베네타",
    "BVLGARI": "불가리",
    "BREITLING": "브라이틀링",
    "Breguet": "브레게",
    "Frederique constant": "브레드릭 콘스탄트",
    "Salvatore Ferragamo": "살바토레 페라가모",
    "Saint Laurent": "생로랑",
    "CHANEL": "샤넬",
    "Celine": "셀린느",
    "Chaumet": "쇼메",
    "Chopard": "쇼파드",
    "Stone Island": "스톤 아일랜드",
    "Stella mccartney": "스텔라 맥카트니",
    "AMI": "아미",
    "Acne": "아크네",
    "A.P.C": "아페쎄",
    "Alexander Mcqueen": "알렉산더 맥퀸",
    "Alexander Wang": "알렉산더 왕",
    "Herno": "에르노",
    "HERMES": "에르메스",
    "ETRO": "에트로",
    "Jaeger LeCoultre": "예거 르쿨트르",
    "Audemars Piguet": "오데마 피게",
    "OMEGA": "오메가",
    "Off White": "오프화이트",
    "HUBLOT": "위블로",
    "Isabel Marant": "이자벨마랑",
    "Givenchy": "지방시",
    "CHRONO SWISS": "크로노 스위스",
    "Christian Dior": "크리스찬 디올",
    "Tag heuer": "태그 호이어",
    "Tod's": "토즈",
    "THOM BROWNE": "톰브라운",
    "Tiffany & Co.": "티파니앤코",
    "CANADA-GOOSE": "캐나다구스",
    "PATEK PHILIPPE": "파텍 필립",
    "Ferragamo": "페라가모",
    "FENDI": "펜디",
    "PRADA": "프라다",
    "Franck Muller": "프랭크 뮬러",
    "FRED": "프레드",
    "Piaget": "피아제",
    "Harry Winston": "해리윈스턴",
    "HAMILTON": "해밀턴",
    "Fredrique Constant": "프레드릭 콘스탄트",
    "Philipp Plein": "필립 플레인",
    "etc.": "기타"
}
brands = {
    "CP컴퍼니": "CP Company",
    "씨피컴퍼니": "CP Company",  
    "IWC": "IWC",
    "아이더블유씨": "IWC",  
    "MSGM": "MSGM",
    "엠에스지엠": "MSGM",  
    "겐조": "Kenzo",
    "켄조": "Kenzo",  
    "고야드": "GOYARD",
    "고야르": "GOYARD",  
    "골든구스": "Golden Goose",
    "골든그스": "Golden Goose",  
    "구찌": "GUCCI",
    "구치": "GUCCI",  
    "그랜드 세이코": "GRAND SEIKO",
    "그랜드세이코": "GRAND SEIKO",  
    "까르띠에": "Cartier",
    "카르티에": "Cartier",  
    "꼼데가르송": "COMME des GARCONS",
    "콤데가르송": "COMME des GARCONS",  
    "끌로에": "Chloe",
    "클로에": "Chloe",  
    "노비스": "Novis",
    "노빅스": "Novis",  
    "닐바렛": "Neil Barrett",
    "닐배럿": "Neil Barrett",  
    "다미아니": "DAMIANI",
    "다미애니": "DAMIANI",  
    "돌체앤가바나": "Dolce & Gabbana",
    "돌체앤가바나": "Dolce & Gabbana",  
    "디스퀘어드": "Dsquared2",
    "디스퀘어드2": "Dsquared2",  
    "랑방": "LANVIN",
    "랑밤": "LANVIN",  
    "로로피아나": "Loro Piana",
    "로로피애나": "Loro Piana",  
    "로에베": "LOEWE",
    "로웨베": "LOEWE",  
    "로저 드뷔": "ROGER DUBUIS",
    "로제 드뷔": "ROGER DUBUIS",  
    "로저비비에": "Rogervivier",
    "로저비비애": "Rogervivier",  
    "론진": "Longines",
    "롱진": "Longines",  
    "롤렉스": "Rolex",
    "로렉스": "Rolex",  
    "루이비통": "LOUIS VUITTON",
    "루이뷔통": "LOUIS VUITTON",  
    "마르니": "Marni",
    "막스마라": "MaxMara",
    "멀버리": "Mulberry",
    "메종마르지엘라": "Maison margiela",
    "메종키츠네": "Maison Kitsuné",
    "무스너클": "Mooseknuckles",
    "모스키노": "Moschino",
    "몽블랑": "MontBlane",
    "몽클레어": "MONCLERE",
    "미우미우": "Miu Miu",
    "바쉐론 콘스탄틴": "Vacheron constantin",
    "반클립 앤 아펠": "Van Cleef & Arpels",
    "발렉스트라": "Valexstra",
    "발렌시아가": "BALENCIAGA",
    "발렌티노": "Valentino",
    "발리": "BALLY",
    "발망": "Balmain",
    "버버리": "Burberrys",
    "베르사체": "Versace",
    "보테가 베네타": "Bottega Veneta",
    "불가리": "BVLGARI",
    "브라이틀링": "BREITLING",
    "브레게": "Breguet",
    "브레드릭 콘스탄트": "Frederique constant",
    "살바토레 페라가모": "Salvatore Ferragamo",
    "생로랑": "Saint Laurent",
    "샤넬": "CHANEL",
    "셀린느": "Celine",
    "쇼메": "Chaumet",
    "쇼파드": "Chopard",
    "스톤 아일랜드": "Stone Island",
    "스텔라 맥카트니": "Stella mccartney",
    "아미": "AMI",
    "아크네": "Acne",
    "아페쎄": "A.P.C",
    "알렉산더 맥퀸": "Alexander Mcqueen",
    "알렉산더 왕": "Alexander Wang",
    "에르노": "Herno",
    "에르메스": "HERMES",
    "에트로": "ETRO",
    "예거 르쿨트르": "Jaeger LeCoultre",
    "오데마 피게": "Audemars Piguet",
    "오메가": "OMEGA",
    "오프화이트": "Off White",
    "위블로": "HUBLOT",
    "이자벨마랑": "Isabel Marant",
    "지방시": "Givenchy",
    "크로노 스위스": "CHRONO SWISS",
    "크리스찬 디올": "Christian Dior",
    "클로에": "Chloe",
    "태그 호이어": "Tag heuer",
    "토즈": "Tod's",
    "톰브라운": "THOM BROWNE",
    "티파니앤코": "Tiffany & Co.",
    "캐나다구스": "CANADA-GOOSE",
    "파텍 필립": "PATEK PHILIPPE",
    "페라가모": "Ferragamo",
    "펜디": "FENDI",
    "프라다": "PRADA",
    "프랭크 뮬러": "Franck Muller",
    "프레드": "FRED",
    "피아제": "Piaget",
    "해리윈스턴": "Harry Winston",
    "해밀턴": "HAMILTON",
    "프레드릭 콘스탄트": "Fredrique Constant",
    "필립 플레인": "Philipp Plein",
    "기타": "etc."
}

histories = ["브랜드", "사설", "해당 사항 없음"]

key_name = {
    "brand": "브랜드",
    "product_name": "상품명",
    "purchase_date": "구매일자",
    "repair_history": "수선이력",
    "name": "성함",
    "phone": "연락처"
}

st.markdown(
    """
    <style>
    [data-testid="stHeader"]{
        display: none;
    }
    body {
        touch-action: pan-x pan-y;
    }
    .header {
        max-width: 736px;
        position: fixed;
        margin: 0 auto;
        top: 0;
        left: 0;
        right: 0;
        background-color: #FFFFFF;
        padding: 1rem;
        z-index: 999991;
    }
    [data-testid="stImage"]{
        width: 300px;
    }
    [data-baseweb="title"] {
        margin-bottom: 50px;
    }
    [data-testid="stChatMessage"] {
        padding: 5px;
    }
    .block-container{
        padding-top: 100px;
    }
    [data-testid="stBottomBlockContainer"]{
        padding-bottom: 15px;
    }
    @media (max-width: 578px) {
        .block-container{
            padding-top: 90px;
        }
        [data-testid="stAppViewBlockContainer"] {
            max-width: 100%;
            padding: 4rem 1rem 1rem;
        }
    }
    </style>
    <div class="header">
        <h1>퀘이자 감정 문의 🔍</h1>
    </div>
    """,
    unsafe_allow_html=True
)

if 'stage' not in st.session_state:
    st.session_state.stage = 0

if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'user_info' not in st.session_state:
    st.session_state.user_info = {}

def fuzzy_match_brand(user_input, threshold=80):
    best_match = process.extractOne(user_input, list(brands.keys()))
    if best_match[1] >= threshold:
        return best_match[0]
    
    best_match = process.extractOne(user_input, list(brands.values()))
    if best_match[1] >= threshold:
        return list(brands.keys())[list(brands.values()).index(best_match[0])]
    
    return None

def chat_response(user_input):
    if st.session_state.stage == 0:
        matched_brand = fuzzy_match_brand(user_input)
        if matched_brand:
            st.session_state.user_info['brand'] = f"{matched_brand} ({brands[matched_brand]})"
            st.session_state.stage = 1
            return f"네, {mt_brand[brands[matched_brand]]} ({brands[matched_brand]}) 제품이군요. **상품명**을 알려주시겠어요?"
        else:
            return f"죄송합니다. '{user_input}'와(과) 일치하는 브랜드를 찾지 못했습니다. 다시 선택해주세요: " + ", ".join(brands.keys())
        
    elif st.session_state.stage == 1:
        st.session_state.user_info['product_name'] = user_input
        st.session_state.stage = 2
        return "상품명을 입력해주셔서 감사합니다. 이제 'YYYY-MM-DD' 형식으로 **구매날짜**를 입력해주세요"

    elif st.session_state.stage == 2:
        try:
            date_obj = datetime.datetime.strptime(user_input, '%Y-%m-%d')
            if date_obj > datetime.datetime.now():
                return "미래의 날짜는 입력할 수 없습니다. 올바른 날짜를 'YYYY-MM-DD' 형식으로 다시 입력해주세요."
            st.session_state.user_info['purchase_date'] = user_input
            st.session_state.stage = 3
            return f"구매일자 '**{user_input}**'로 기록했습니다. **수선 이력**이 있나요?  \n('브랜드', '사설', '해당 사항 없음' 중 선택)"
        except ValueError:
            return "날짜 형식이 올바르지 않습니다. 'YYYY-MM-DD' 형식으로 다시 입력해주세요."

    elif st.session_state.stage == 3:
        if user_input in histories:
            st.session_state.user_info['repair_history'] = user_input
            st.session_state.stage = 4
            return f"수선 이력 '(**{user_input}**)' 기록했습니다. 고객님의 **성함**을 알려주세요."
        else:
            return "입력이 올바르지 않습니다. '브랜드', '사설', '해당 사항 없음' 중에서 선택해주세요."

    elif st.session_state.stage == 4:
        st.session_state.user_info['name'] = user_input
        st.session_state.stage = 5
        return f"{user_input}님, 반갑습니다. 고객님의 **연락처**를 알려주세요."

    elif st.session_state.stage == 5:
        st.session_state.user_info['phone'] = user_input
        st.session_state.stage = 6
        return "마지막으로 제품의 **전체 사진**과 **구성품 사진**을 업로드해주세요"

    elif st.session_state.stage == 7:
        if user_input.lower() == '확인':
            st.session_state.stage = 8
            return "감사합니다. 신청이 완료되었습니다. 추가로 궁금한 점이 있으시면 언제든 물어보세요."
        elif user_input.lower() == '수정':
            st.session_state.stage = 0
            return "네, 처음부터 다시 시작하겠습니다. 브랜드를 선택해주세요."
        else:
            return "입력이 올바르지 않습니다. '확인' 또는 '수정'이라고 입력해주세요."
 
    elif st.session_state.stage == 8:
        return random.choice([
            "더 궁금한 점이 있으신가요?",
            "다른 문의사항이 있으시면 말씀해주세요.",
            "추가 질문이 있으시다면 언제든 물어보세요."
        ])

for message in st.session_state.messages:
    if message["role"] == "assistant":
        with st.chat_message("assistant", avatar="./static/images/icon/icon2.svg"):
            st.markdown(message["content"])
    else:
        with st.chat_message("user", avatar="https://api.dicebear.com/9.x/adventurer-neutral/svg?seed=Peanut"):
            st.markdown(message["content"])

if st.session_state.stage == 0 and not st.session_state.messages:
    st.chat_message("assistant", avatar="./static/images/icon2.svg").markdown("안녕하세요! 퀘이자 감정 문의 서비스입니다.  \n**어떤 브랜드의 제품**을 감정받고 싶으신가요?  \nex)구찌,디올,샤넬,루이비통,프라다,펜디 등")
    st.session_state.messages.append({"role":"assistant", "content": "안녕하세요! 퀘이자 감정 문의 서비스입니다.  \n**어떤 브랜드의 제품**을 감정받고 싶으신가요?  \nex)구찌,디올,샤넬,루이비통,프라다,펜디 등"})

if prompt := st.chat_input("여기에 메시지를 입력하세요."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="https://api.dicebear.com/9.x/adventurer-neutral/svg?seed=Peanut"):
        st.markdown(prompt)

    response = chat_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant", avatar="./static/images/icon2.svg"):
        st.markdown(response)

if st.session_state.stage == 6:
    uploaded_files = st.file_uploader("이미지를 여기에 업로드하세요.", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])
    if uploaded_files:
        cols = st.columns(len(uploaded_files))
        for i, file in enumerate(uploaded_files[:len(uploaded_files)]):
            with cols[i]:
                image = Image.open(file)
                st.image(image, caption='업로드된 이미지', use_column_width=True)
        st.session_state.user_info['images'] = uploaded_files
        info_summary = "  \n".join([f"**{key_name[key]}**: {value}" for key, value in st.session_state.user_info.items() if key != "images"])
        st.chat_message("assistant", avatar="./static/images/icon2.svg").markdown(f"입력하신 정보를 확인해주세요:  \n  \n{info_summary}  \n  \n모든 정보가 정확하다면 '**확인**'이라고 입력해주세요.  \n수정이 필요하다면 '**수정**'이라고 입력해주세요.")
        st.session_state.stage = 7
