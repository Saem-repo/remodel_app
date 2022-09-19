import streamlit as st


def search_menu () :
    st.markdown('1. 건물 개요')

    bldg_cols = st.columns(7)

    
    with bldg_cols[0] :
        bldg_info_1 = st.selectbox(
        '설계/시공',
        ('설계', '시공')
        )
    
    with bldg_cols[1] :
        bldg_info_2 = st.selectbox(
        '건물유형',
        ('단독주택(1)', '공동주택(2)', '음식영업시설(2)',
        '문화집회시설(4)', '종교시설(5)', '판매시설(6)',
        '의료시설(7)', '교육연구시설(8)', '노유자시설(9)',
        '수련시설(10)', '운동시설(11)', '업무시설(12)',
        '숙박시설(13)', '위락시설(14)', '공장시설(15)',
        '교정 및 군사시설(16)', '기타시설(17)')
        )

    with bldg_cols[2] :
        bldg_info_3 = st.selectbox(
        '소재지 (한국)',
        ('중부1권역(1)', '중부2권역(2)', '남부권역(3)', '제주권역(4)')
        )
    
    with bldg_cols[3] : # 그림 보고 입력할수 있게
        bldg_info_4 = st.text_input('소재지 (해외)', "국가 ISO 번호 입력", max_chars=100)
        
    with bldg_cols[4] : # 그림 보고 입력할수 있게
        bldg_info_5 = st.text_input('기후권역 (쾨펜 기후대)', "기후대 분류 기준 입력", max_chars=100)
            
    with bldg_cols[5] :
        bldg_info_6 = st.text_input("연면적", "단일값, 범위값", max_chars=100)
    
    with bldg_cols[6] :
        bldg_info_7 = st.selectbox(
        '구조방식',
        ('목구조', '조적조', '철골구조', '철근콘크리트구조', '복합구조')
        )

    st.markdown('---')

    st.markdown('2. 리모델링 개요')

    remodel_cols = st.columns(7)

    with remodel_cols[0] : # 그림 보고 입력할수 있게
        remodel_info_1 = st.text_input('리모델링 연도', "4자리 연도 입력", max_chars=100)
            
    with remodel_cols[1] :
        remodel_info_2 = st.text_input("리모델링 비용", "단일값, 범위값 (원단위 입력)", max_chars=100)

    st.markdown('---')

    st.markdown('3. 리모델링 대상')
    
    st.markdown('- 패시브시스템')

    remodel_passive_cols = st.columns(9)

    with remodel_passive_cols[0] :
        remodel_passive_info_1 = st.selectbox(
        '벽체단열',
        ('설계', '시공')
        )
    
    with remodel_passive_cols[1] :
        remodel_passive_info_2 = st.selectbox(
        '지붕단열',
        ('단독주택(1)', '공동주택(2)', '음식영업시설(2)',
        '문화집회시설(4)', '종교시설(5)', '판매시설(6)',
        '의료시설(7)', '교육연구시설(8)', '노유자시설(9)',
        '수련시설(10)', '운동시설(11)', '업무시설(12)',
        '숙박시설(13)', '위락시설(14)', '공장시설(15)',
        '교정 및 군사시설(16)', '기타시설(17)')
        )

    with remodel_passive_cols[2] :
        remodel_passive_info_3 = st.selectbox(
        '창호개선',
        ('중부1권역(1)', '중부2권역(2)', '남부권역(3)', '제주권역(4)')
        )
    
    with remodel_passive_cols[3] : # 그림 보고 입력할수 있게
        remodel_passive_info_4 = st.selectbox(
        '창프레임단열',
        ('중부1권역(1)', '중부2권역(2)', '남부권역(3)', '제주권역(4)')
        )
        
    with remodel_passive_cols[4] : # 그림 보고 입력할수 있게
        remodel_passive_info_5 = st.selectbox(
        '기밀성강화',
        ('중부1권역(1)', '중부2권역(2)', '남부권역(3)', '제주권역(4)')
        )
            
    with remodel_passive_cols[5] :
        remodel_passive_info_6 = st.selectbox(
        '창호일사제어',
        ('중부1권역(1)', '중부2권역(2)', '남부권역(3)', '제주권역(4)')
        )
    
    with remodel_passive_cols[6] :
        remodel_passive_info_7 = st.selectbox(
        '차양',
        ('목구조', '조적조', '철골구조', '철근콘크리트구조', '복합구조')
        )

    with remodel_passive_cols[7] :
        remodel_passive_info_8 = st.selectbox(
        '자연환기',
        ('목구조', '조적조', '철골구조', '철근콘크리트구조', '복합구조')
        )

    with remodel_passive_cols[8] :
        remodel_passive_info_9 = st.selectbox(
        '자연채광',
        ('목구조', '조적조', '철골구조', '철근콘크리트구조', '복합구조')
        )

    st.markdown('- 액티브시스템')

    remodel_active_cols = st.columns(5)

    with remodel_active_cols[0] :
        remodel_active_info_1 = st.selectbox(
        '난방',
        ('설계', '시공')
        )
    
    with remodel_active_cols[1] :
        remodel_active_info_2 = st.selectbox(
        '냉방',
        ('단독주택(1)', '공동주택(2)', '음식영업시설(2)')
        )

    with remodel_active_cols[2] :
        remodel_active_info_3 = st.selectbox(
        '냉난방',
        ('중부1권역(1)', '중부2권역(2)', '남부권역(3)', '제주권역(4)')
        )
    
    with remodel_active_cols[3] : # 그림 보고 입력할수 있게
        remodel_active_info_4 = st.selectbox(
        '환기',
        ('중부1권역(1)', '중부2권역(2)', '남부권역(3)', '제주권역(4)')
        )
        
    with remodel_active_cols[4] : # 그림 보고 입력할수 있게
        remodel_active_info_5 = st.selectbox(
        '조명시스템',
        ('중부1권역(1)', '중부2권역(2)', '남부권역(3)', '제주권역(4)')
        )

    st.markdown('- 신재생 에너지 시스템')

    remodel_renewable_cols = st.columns(8)

    with remodel_renewable_cols[0] :
        remodel_renewable_info_1 = st.selectbox(
        '태양광시스템',
        ('설계', '시공')
        )
    
    with remodel_renewable_cols[1] :
        remodel_renewable_info_2 = st.selectbox(
        '태양열시스템',
        ('단독주택(1)', '공동주택(2)', '음식영업시설(2)')
        )

    with remodel_renewable_cols[2] :
        remodel_renewable_info_3 = st.selectbox(
        '지열시스템',
        ('중부1권역(1)', '중부2권역(2)', '남부권역(3)', '제주권역(4)')
        )
    
    with remodel_renewable_cols[3] : # 그림 보고 입력할수 있게
        remodel_renewable_info_4 = st.selectbox(
        '풍력시스템',
        ('중부1권역(1)', '중부2권역(2)', '남부권역(3)', '제주권역(4)')
        )
        
    with remodel_renewable_cols[4] : # 그림 보고 입력할수 있게
        remodel_renewable_info_5 = st.selectbox(
        '바이오에너지',
        ('중부1권역(1)', '중부2권역(2)', '남부권역(3)', '제주권역(4)')
        )

    with remodel_renewable_cols[5] :
        remodel_renewable_info_6 = st.selectbox(
        '연료전지',
        ('중부1권역(1)', '중부2권역(2)', '남부권역(3)', '제주권역(4)')
        )
    
    with remodel_renewable_cols[6] : # 그림 보고 입력할수 있게
        remodel_renewable_info_7 = st.selectbox(
        '소형열병합',
        ('중부1권역(1)', '중부2권역(2)', '남부권역(3)', '제주권역(4)')
        )
        
    with remodel_renewable_cols[7] : # 그림 보고 입력할수 있게
        remodel_renewable_info_8 = st.selectbox(
        '에너지저장장치',
        ('중부1권역(1)', '중부2권역(2)', '남부권역(3)', '제주권역(4)')
        )

    st.markdown('---')

    st.markdown('4. 리모델링 효과')

    remodel_result_cols = st.columns(3)

    with remodel_result_cols[0] :
        remodel_result_info_1 = st.text_input("에너지 저감율(%)", "단일값, 범위값 (퍼센트 입력)", max_chars=100)

    with remodel_result_cols[1] :
        remodel_result_info_2 = st.text_input("이산화탄소 배출량 감소율(%)", "단일값, 범위값 (퍼센트 입력)", max_chars=100)
    
    with remodel_result_cols[2] :
        remodel_result_info_3 = st.text_input("생애주기비용 저감율(%)", "단일값, 범위값 (퍼센트 입력)", max_chars=100)

    
    # 건물 개요에 대한 사용자 입력 값 리스트
    bldg_info_list = [bldg_info_1,bldg_info_2,bldg_info_3,bldg_info_4,bldg_info_5,bldg_info_6,bldg_info_7]
    
    # 리모델링 정보에 대한 사용자 입력 값 리스트
    remodel_info_list = [remodel_info_1,remodel_info_2]

    # 리모델링 패시브 시스템 대한 사용자 입력 값 리스트
    remodel_passive_info_list = [remodel_passive_info_1, remodel_passive_info_2, remodel_passive_info_3,
                                 remodel_passive_info_4, remodel_passive_info_5, remodel_passive_info_6,
                                 remodel_passive_info_7, remodel_passive_info_8, remodel_passive_info_9]
    
    # 리모델링 액티브 시스템 대한 사용자 입력 값 리스트
    remodel_active_info_list = [remodel_active_info_1, remodel_active_info_2, remodel_active_info_3,
                                remodel_active_info_4, remodel_active_info_5]
    
    # 리모델링 신재생 시스템 대한 사용자 입력 값 리스트
    remodel_renewable_info_list = [remodel_renewable_info_1,remodel_renewable_info_1,remodel_renewable_info_1,
                                   remodel_renewable_info_4,remodel_renewable_info_5,remodel_renewable_info_6,
                                   remodel_renewable_info_7,remodel_renewable_info_8
                                   ]

    # 리모델링 결과에 대한 사용자 입력 값 리스트
    remodel_result_info_list = [remodel_result_info_1,remodel_result_info_2,remodel_result_info_3]

    
    return bldg_info_list, remodel_info_list, remodel_passive_info_list, remodel_active_info_list, remodel_renewable_info_list, remodel_result_info_list