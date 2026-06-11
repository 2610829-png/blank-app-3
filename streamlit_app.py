import streamlit as st

st.title("🔐 암호 맞추기 게임")

# 세션 상태 초기화
if 'current_stage' not in st.session_state:
    st.session_state.current_stage = 0  # 0: 첫번째 입력 (3), 1: 두번째 입력 (2), 2: 세번째 입력 (1)
    st.session_state.message = ""

# 정답
password = [3, 2, 1]
stage_names = ["첫 번째", "두 번째", "세 번째"]

# 게임 상태 표시
st.write(f"### 진행 상황: {st.session_state.current_stage}/3")
st.write(f"**{stage_names[st.session_state.current_stage]} 자릿수를 입력하세요!**")

# 1, 2, 3 중 선택
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("1", key=f"btn_1_{st.session_state.current_stage}"):
        if 1 == password[st.session_state.current_stage]:
            if st.session_state.current_stage < 2:
                st.session_state.current_stage += 1
                st.session_state.message = "✅ 정답! 다음 자릿수를 입력하세요."
            else:
                st.session_state.message = "🎉 암호 321을 완성했습니다! 축하합니다!"
                st.balloons()
            st.rerun()
        else:
            st.session_state.current_stage = 0
            st.session_state.message = "❌ 틀렸습니다! 처음부터 다시 시작합니다."
            st.rerun()

with col2:
    if st.button("2", key=f"btn_2_{st.session_state.current_stage}"):
        if 2 == password[st.session_state.current_stage]:
            if st.session_state.current_stage < 2:
                st.session_state.current_stage += 1
                st.session_state.message = "✅ 정답! 다음 자릿수를 입력하세요."
            else:
                st.session_state.message = "🎉 암호 321을 완성했습니다! 축하합니다!"
                st.balloons()
            st.rerun()
        else:
            st.session_state.current_stage = 0
            st.session_state.message = "❌ 틀렸습니다! 처음부터 다시 시작합니다."
            st.rerun()

with col3:
    if st.button("3", key=f"btn_3_{st.session_state.current_stage}"):
        if 3 == password[st.session_state.current_stage]:
            if st.session_state.current_stage < 2:
                st.session_state.current_stage += 1
                st.session_state.message = "✅ 정답! 다음 자릿수를 입력하세요."
            else:
                st.session_state.message = "🎉 암호 321을 완성했습니다! 축하합니다!"
                st.balloons()
            st.rerun()
        else:
            st.session_state.current_stage = 0
            st.session_state.message = "❌ 틀렸습니다! 처음부터 다시 시작합니다."
            st.rerun()

# 메시지 표시
if st.session_state.message:
    if "✅" in st.session_state.message:
        st.success(st.session_state.message)
    elif "🎉" in st.session_state.message:
        st.success(st.session_state.message)
    else:
        st.error(st.session_state.message)

# 리셋 버튼
if st.button("🔄 게임 리셋"):
    st.session_state.current_stage = 0
    st.session_state.message = ""
    st.rerun()
