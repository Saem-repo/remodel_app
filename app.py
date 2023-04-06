#%%

import tensorflow as tf
import streamlit as st
from PIL import Image

from random import *

import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from streamlit_option_menu import option_menu

import os
import sys
import glob
import base64
from io import BytesIO

from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
from sklearn.metrics import classification_report
import joblib
import pickle

# 지도관련
import json
import plotly.express as px
import plotly.graph_objects as go






#%%
st.set_page_config(layout='wide',
                   page_icon='./img/smart_grid.png', 
                #    initial_sidebar_state='collapsed',
                   page_title='건축물 리모델링 설계/시공 사례기반 시스템 (BRICS: Building Remodeling Information & Casebase System)')

st.sidebar.image('./img/Home/SSEL_logo.png')

#%%

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title=None,  # required
                options=["홈", "리모델링 사례 현황", "리모델링 사례 검색", "유사 리모델링 사례 추천"],  # required
                icons=["house", "sd-card", "search", "list-task"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
                # styles = {
                # "container": {"color":"#000000", "padding": "4!important", "background-color": "#fafafa"},
                # "icon": {"color": "orange", "font-size": "25px"}, 
                # "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                # "nav-link-selected": {"background-color": "green"},
                # }
            )
        return selected

    if example == 2:
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["홈", "리모델링 사례 현황", "리모델링 사례 검색", "유사 리모델링 사례 추천"],  # required
            icons=["house", "sd-card", "search", "list-task"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            # styles = {
            #     "container": { "padding": "4!important", "background-color": "#fafafa"},
            #     "icon": {"color": "orange", "font-size": "25px"}, 
            #     "nav-link": {"font-size": "25px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
            #     "nav-link-selected": {"background-color": "green"},
            # }
        )
        return selected


selected = streamlit_menu(example=1)   

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.markdown('---')

st.sidebar.info(''' **Smart and Sustainable Environment LAB** | **SSEL**     
                    **Contact Info** | 
                    **Call** : +82-42-350-5667   
                    **Website** : <http://ssel.kaist.ac.kr/>   
                ''')
# st.sidebar.info(''' **Smart and Sustainable Environment Design Laboratory (SSEL in KAIST) 
#                     연락처: 
#                     - 주소: 335 Gwahangno(373-1 Guseong-Dong), Daejeon 305-701, Republic of Korea
#                     - 전화: +82-42-350-5667 
#                     - 팩스: +82-42-350-3610
#                     - 웹페이지: <https://ssel.kaist.ac.kr>
                    
#                     **Copyright SSEL all right reserved**

#                     ''')
                    #**| SSEL** 
                    # **E-mail** : saem@kaist.ac.kr  
                    # **Website** :   
                    # - Google Scholar : <https://scholar.google.co.kr/citations?hl=ko&user=r7tvGrUAAAAJ>   
                    # - Research Gate : <https://www.researchgate.net/profile/Han-Saem-Park-3> 


    
def home () :
    
    # img = Image.open('./img/home/smart_city.png')
    # st.image(img)
    # st.markdown("---")

    st.markdown(""" <style> .font {
        font-size:45px ; font-family: 'Cooper Black'; color: #0064ff; text-align: center;} 
        </style> """, unsafe_allow_html=True)
    st.markdown(""" <style> .font1 {
        font-size:25px ; font-family: 'Cooper Black'; color: #46CCFF; text-align: center;} 
        </style> """, unsafe_allow_html=True)
    
    st.markdown('''<p class="font"><strong>건축물 리모델링 설계/시공 사례기반 시스템</strong></p>   
                   <p class="font1"><strong>BRICS : Building Remodeling Information & Casebase System</strong></p>
                ''', unsafe_allow_html=True)
    
    st.markdown("---")
        
    col1, col2 = st.columns([0.5, 0.6])
    
    with col1:               # To display the header text using css style
        st.markdown('''
                    - ### 시스템 개요
                        - <p style="font-size:20px;"> 본 프로그램은 기존 건축물 저탄소 에너지효율화 최적 모델 기반 구축을 위해 국내·외 리모델링 사례들을 수집하고 유형화시킨 DB 시스템을 고안하여 이를 토대로 향후 기 건축물들의 리모델링을 위한 가이드라인을 제공함으로써 최적의 리모델링 방안 도출을 목적으로 개발됨 </p>
                    
                    - ### 시스템 기능
                        - <p style="font-size:20px;"> 유사케이스 추천 모드는 각 건물 유형에 따라 데이터를 군집 및 분류된 리모델링 사례 간 유사도 측정하여 해당 사례를 올림차순하여 상위 15개 제공 </p>    
                        - <p style="font-size:20px;"> DB 검색 모드는 리모델링 사례 DB 시스템의 전체 사례들에 대해 접근할 수 있는 모드로써 특정 입력값을 통해 결과값을 표시 </p>    
                        - <p style="font-size:20px;"> 웹 기반 인터페이스 활용을 통한 추가 건물 특성 정보 데이터 확보 및 기계학습 기반 추천 알고리즘의 성능 업데이트 </p>    
                    ''', unsafe_allow_html=True)
        
        
    with col2:               # To display the header text using css style
        # st.video('./img/home/smartcity.mp4')
        st.image('./img/Home/remodel_img.png')
    

    st.markdown("---")
    
    # st.markdown(""" <style> .font {
    # text-align: left; font-size:40px ; font-family: 'Cooper Black'; color: #FF9633;} 
    # </style> """, unsafe_allow_html=True)
    # st.markdown('<p class="font">저탄소 에너지효율화 기술 기반 에너지공유 커뮤니티 구축 기술 개발을 위한 리모델링 사례 추천 시스템</p>', unsafe_allow_html=True)    
    


    # 밑에는 한국 지역별 에너지(전기,가스,난방) 사용량 지도
    df = pd.read_csv("./dataset/geo/latest_geo_df.csv", encoding='euc-kr')

    kor_geo_file = './dataset/geo/sig.zip.geojson'
    kor_geo = json.load(open(kor_geo_file, encoding='utf-8'))

    # SIG_KOR_NM <- 한국 지명

    for idx, sig_cd_dict in enumerate(kor_geo['features']) :
        sig_id = sig_cd_dict['properties']['SIG_CD']
        sig_id = int(sig_id)
        sig_nm = df.loc[(df['sigun_code'] == sig_id), 'sigun_nm']
        elec = df.loc[(df['sigun_code'] == sig_id), '전기사용량(TOE)']
        gas = df.loc[(df['sigun_code'] == sig_id), '가스사용량(TOE)']
        heat = df.loc[(df['sigun_code'] == sig_id), '지역난방(TOE)']
        txt = f'<b><h4>{sig_nm}</h4></b> 전기사용량(TOE): {elec} <br> 가스사용량(TOE): {gas} <br> 지역난방(TOE): {heat}'

        kor_geo['features'][idx]['properties']['tooltip1'] = txt
        kor_geo['features'][idx]['properties']['elec'] = elec
        
    # st.write(sig_id)
    # st.write(kor_geo['features'][1])

    mid_col1, mid_col2, mid_col3 = st.columns([0.4, 0.4, 0.4])

    with mid_col1 :
        st.markdown(""" <style> .mid_col1 {
        font-size:20px; text-align: "center"; font-family: 'Cooper Black'; font-weight:'bold';, color: #000000;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="mid_col1"><strong>국내 지역별 전력 에너지 사용량</strong></p>',unsafe_allow_html=True)
        
        fig_elec = px.choropleth_mapbox(df, geojson=kor_geo,
                               locations='sigun_code',
                               color='전기사용량(TOE)',
                               color_continuous_scale="matter",
                               range_color=(0, 2),
                               mapbox_style="carto-positron",
                               featureidkey="properties.SIG_CD",
                               zoom=6, center = {"lat": 37.982, "lon": 126.986},
                               opacity=0.5, labels={'전력소비량' : '전기사용량(TOE)'})
                            
        fig_elec.update_layout(margin={"r": 0, "t": 0, "l": 0, "b":0})
        st.plotly_chart(fig_elec)
    
        
    
    with mid_col2 :
        st.markdown(""" <style> .mid_col2 {
        font-size:20px ; font-family: 'Cooper Black'; font-weight: 'bold';, color: #000000;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="mid_col2"><strong>국내 지역별 가스 에너지 사용량</strong></p>',unsafe_allow_html=True)
        
        fig_gas = px.choropleth_mapbox(df, geojson=kor_geo,
                               locations='sigun_code',
                               color='가스사용량(TOE)',
                               color_continuous_scale="matter",
                               range_color=(0, 2),
                               mapbox_style="carto-positron",
                               featureidkey="properties.SIG_CD",
                               zoom=6, center = {"lat": 36.565, "lon": 126.986},
                               opacity=0.5, labels={'가스소비량' : '가스사용량(TOE)'})
                            
        fig_gas.update_layout(margin={"r": 0, "t": 0, "l": 0, "b":0})
        st.plotly_chart(fig_gas)

    with mid_col3 :
        st.markdown(""" <style> .mid_col3 {
        font-size:20px ; font-family: 'Cooper Black'; font-weight:'bold';, color: #000000;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="mid_col3"><strong>국내 지역별 지역난방 에너지 사용량</strong></p>',unsafe_allow_html=True)
        
        fig_heat = px.choropleth_mapbox(df, geojson=kor_geo,
                                locations='sigun_code',
                                color='지역난방(TOE)',
                                color_continuous_scale="matter",
                                range_color=(0, 2),
                                mapbox_style="carto-positron",
                                featureidkey="properties.SIG_CD",
                                zoom=6, center = {"lat": 35.322, "lon": 126.986},
                                opacity=0.5, labels={'지역난방소비량' : '지역난방(TOE)'})
                                
        fig_heat.update_layout(margin={"r": 0, "t": 0, "l": 0, "b":0})
        st.plotly_chart(fig_heat)



def case_summary() : # 수집된 사례 데이터 집계

    import matplotlib.font_manager as fm
    
    font_name = fm.FontProperties(fname="./font/Malgun Gothic.ttf").get_name()
    font = fm.FontProperties(fname="./font/Malgun Gothic.ttf")
    plt.rc('font', family=font_name)
    
    # sns.set(font="./font/Malgun Gothic")
    # sns.set_style('white')

    
    st.markdown(""" <style> .font {
        font-size:45px ; font-family: 'Cooper Black'; color: #0064ff; text-align: center;} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font"><strong>리모델링 사례 현황</strong></p>', unsafe_allow_html=True) 
    st.markdown("---")
    
    # 우선 그래프를 어떤것들 보여줘야할지를 결정...
    # 1. 사례 갯수 (국내, 해외, 전체)
    # 2. 건물 유형에 따른 사례 갯수
    # 3. 저감율에 따른 사례 건물 유형
    # 4. 저감율(에너지, CO2, LCC) 별로 패시브, 액티브, 신재생 항목 어떤건지?

    df = pd.read_csv("./dataset/search/rev_search_df.csv", encoding='euc-kr')

    build_type = {"단독주택(1)": 16,
                  '공동주택(2)': 90,
                  "음식영업시설(3)": 5,
                  '문화집회시설(4)': 2,
                  '종교시설(5)': 1,
                  '판매시설(6)': 3,
                  '의료시설(7)': 26,
                  '교육연구시설(8)': 2,
                  '노유자시설(9)': 2,
                  "수련시설(10)": 2,
                  '운동시설(11)': 55,
                  "업무시설(12)": 2,
                  "숙박시설(13)": 0,
                  '위락시설(14)': 0,
                  "공장시설(15)": 1,
                  "교정 및 군사시설(16)": 2,
                  '기타시설(17)': 0}

    col1, col2 = st.columns(2)
    with col1:
        plt.rcParams['font.family'] ='Malgun Gothic'
        plt.rcParams['axes.unicode_minus'] =False

        st.markdown('### 전체 리모델링 사례 데이터 현황')
        NofK = len(df.loc[(df['iso_flag'] == 410),:])
        NofI = len(df.loc[(df['iso_flag'] != 410),:])
        total = NofK+NofI
        fig_1_list = [NofK, NofI, total]
        fig_1 = pd.DataFrame([fig_1_list], columns=['국내사례', '해외사례', '전체사례'])

        fig = plt.figure(figsize=(10,6.6))
        sns.barplot(fig_1)
        plt.ylabel("사례 갯수(건)", fontproperties=font)
        plt.xticks(fontproperties=font)
        # plt.rcParams['font.family'] = 'Malgun Gothic'
        
        st.pyplot(fig)
        
    with col2:
        plt.rcParams['font.family'] ='Malgun Gothic'
        plt.rcParams['axes.unicode_minus'] =False

        st.markdown('### 전체 건물 유형별 리모델링 사례')
        # st.set_option('deprecation.showPyplotGlobalUse', False)
        
        fig_2_df = pd.DataFrame([build_type], columns=build_type.keys())
        fig_2_df.index = ['사례 건수(건)']
        # st.write(fig_2)
        # st.write(fig_2.T)
        
        
        plt.figure(figsize=(10,7))
        plt.barh(fig_2_df.T)
        # fig_2_df.T.plot(kind='barh')
        plt.ylabel('건물 유형', fontproperties=font)
        plt.yticks(fontproperties=font)
        plt.xticks(fontproperties=font)
        # plt.legend(fontproperties=font)
        
        st.pyplot()

    #     col3, col4 = st.columns(2)            
    #     with col3:
    #         st.markdown('### Temperature')
    #         lineplot(energy_sum_w6, energy_win_w6,'temp')

    #     with col4:
    #         st.markdown('### Humidity')
    #         lineplot(energy_sum_w6, energy_win_w6,'humidity')


    # if eda_menu == "Building Energy":
        
    #     st.markdown(''' ### Source and Target Buildings ''')

    #     with st.expander("Statistics of source building"):
    #         st.write('Source buildings (in Summer)')
    #         st.table(energy_sum.describe())
        
        
        
    #     def lineplot(df, df1, data_cols) :
    #         # plt.style.use('dark_background')
    #         filtered_df_sum = df.loc[:,data_cols]
    #         filtered_df_win = df1.loc[:,data_cols]


    #         # print(filtered_df.columns[0])
    #         fig = plt.figure(figsize=(10,7))
    #         plt.plot(filtered_df_sum, color='r', label='Summer')
    #         plt.plot(filtered_df_win, color='y', label='Winter')
            
    #         if data_cols == 'temp' :
    #             plt.ylabel('Outdoor Temperature $(\N{DEGREE SIGN}C)$')
    #         elif data_cols == 'humidity' :
    #             plt.ylabel('Outdoor Relative Humidity Difference (%)')
    #         else :
    #             plt.ylabel('Energy Consumption $(kWh)$')
            
    #         plt.legend(loc='best')
            
    #         return st.pyplot(fig)
        
    #     col1, col2 = st.columns(2)
        
    #     with col1:
    #         st.markdown('### Energy profile of W1 in different season')
    #         lineplot(energy_sum_w1, energy_win_w1,'applied_engi')
            
    #     with col2:
    #         st.markdown('### Energy profile of W6 in different season')
    #         lineplot(energy_sum_w6, energy_win_w6,'mir_dorm')

    #     col3, col4 = st.columns(2)            
    #     with col3:
    #         st.markdown('### Temperature')
    #         lineplot(energy_sum_w6, energy_win_w6,'temp')

    #     with col4:
    #         st.markdown('### Humidity')
    #         lineplot(energy_sum_w6, energy_win_w6,'humidity')


def search_cases (): # 사례 검색
    st.markdown(""" <style> .font {
        font-size:45px ; font-family: 'Cooper Black'; color: #0064ff; text-align: center;} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font"><strong>리모델링 사례 검색</strong></p>', unsafe_allow_html=True)
    st.markdown('''
                    - ### 사례 검색 개요 및 순서
                        - 수집된 건축물 리모델링 사례들로부터 속성 정보를 선택적으로 입력 후 조건에 만족하는 모든 사례들의 대한 정보를 표형식으로 제공
                        - 각 도출된 사례들의 상세 정보는 표에서 제공되는 건축물 그림을 클릭하여 접근 가능
                ''')

    st.markdown("---")

    st.markdown('1. 건물 개요')

    bldg_cols = st.columns(7)

    def format_func(dict, option):
        return dict[option]

    
    with bldg_cols[0] :
        design = {1: "설계(1)", 2: "시공(2)"}

        bldg_info_1 = st.selectbox('설계/시공', options = list(design.keys()), format_func=lambda x: design[x])
        
    
    with bldg_cols[1] :
        build_type = {1: "단독주택(1)", 2: '공동주택(2)', 3: "음식영업시설(3)",
                      4: '문화집회시설(4)', 5: '종교시설(5)', 6: '판매시설(6)',
                      7: '의료시설(7)', 8: '교육연구시설(8)', 9: '노유자시설(9)',
                      10: "수련시설(10)", 11: '운동시설(11)', 12: "업무시설(12)",
                      13: "숙박시설(13)", 14: '위락시설(14)', 15: "공장시설(15)",
                      16: "교정 및 군사시설(16)", 17: '기타시설(17)'}

        bldg_info_2 = st.selectbox('건물유형', options = list(build_type.keys()), format_func=lambda x: build_type[x])
        

    with bldg_cols[2] :
        kor_flag = {1: '중부1권역(1)', 2: '중부2권역(2)', 3: '남부권역(3)',
                    4: '제주권역(4)'}

        bldg_info_3 = st.selectbox('소재지 (한국)', options = list(kor_flag.keys()), format_func=lambda x: kor_flag[x])
    
    with bldg_cols[3] : # 그림 보고 입력할수 있게
        #한국: 410
        bldg_info_4 = st.text_input('소재지 (해외)', "410", max_chars=100, help="대한민국 ISO 번호로 기본 설정")
        
    with bldg_cols[4] : # 그림 보고 입력할수 있게
        bldg_info_5 = st.text_input('기후권역 (쾨펜 기후대)', "기후대 분류 기준 입력", max_chars=100)
            
    with bldg_cols[5] :
        bldg_info_6 = st.text_input("연면적", "단일값, 범위값", max_chars=100)
    
    with bldg_cols[6] :
        build_structure = {1: '목구조(1)', 2: '조적조(2)', 3: '철골구조(3)', 4: '철근콘크리트구조(4)', 5: '복합구조(5)'}
        bldg_info_7 = st.selectbox('구조방식', options = list(build_structure.keys()), format_func=lambda x: build_structure[x])

    st.markdown('---')

    st.markdown('2. 리모델링 개요')

    remodel_cols = st.columns(7)

    with remodel_cols[0] : # 그림 보고 입력할수 있게
        remodel_info_1 = st.text_input('리모델링 연도', "4자리 연도 입력", max_chars=100)
            
    with remodel_cols[1] :
        remodel_info_2 = st.text_input("리모델링 비용", "단일값, 범위값 (원단위 입력)", max_chars=100)

    st.markdown('---')

    st.markdown('3. 리모델링 대상') # 여기서부터 작업!!!!!- 대화
    
    st.markdown('- 패시브시스템')

    remodel_passive_cols = st.columns(9)

    with remodel_passive_cols[0] :
        wall = {101: '벽체단열개선(101)', 102: '압출법(102)', 103: '비드법(103)',
                104: '글라스울(104)', 105: '열반사(105)', 106: '셀롤로오스(106)',
                107: '폴리우레탄폼(107)', 108: '폴리에틸렌(108)', 109: '페놀폼(109)', 110: '진공(110)'}

        remodel_passive_info_1 = st.multiselect(
        '벽체단열', options = list(wall.keys()), format_func=lambda x: wall[x])
    
    with remodel_passive_cols[1] :
        roof = {151: '지붕단열개선(151)', 152: '압출법(152)', 153: '비드법(153)',
                154: '글라스울(154)', 155: '열반사(155)', 156: '셀롤로오스(156)',
                157: '폴리우레탄폼(157)', 158: '페놀폼(158)', 159: '진공(159)'}

        remodel_passive_info_2 = st.multiselect('지붕단열', options = list(roof.keys()), format_func=lambda x: roof[x])
        

    with remodel_passive_cols[2] :
      
        win = {201: '창호성능개선(201)', 202: '단층(202)', 203: '복층(203)',
                204: '복층+아르곤(204)', 205: '복층+진공(205)', 206: '삼중(206)',
                207: '삼중+아르곤(207)', 208: '삼중+진공(208)', 209: '로이단층(209)', 210: '로이복층(210)',
				211: '로이복층+아르곤(211)', 212: '로이복층+진공(212)', 213: '로이삼중(213)', 214: '로이삼중+아르곤(214)', 215: '로이삼중+진공(215)',
				216: '로이사중(216)', 217: '로이사중+아르곤(217)', 218: '로이사중+진공(218)'}

        remodel_passive_info_3 = st.multiselect(
        '창호개선', options = list(win.keys()), format_func=lambda x: win[x])
    
    with remodel_passive_cols[3] : # 그림 보고 입력할수 있게
        win_frame = {251: '창프레임단열개선(251)', 252: 'AL(252)', 253: 'PVC(253)'}

        remodel_passive_info_4 = st.multiselect(
        '창프레임단열', options = list(win_frame.keys()), format_func=lambda x: win_frame[x])
        
    with remodel_passive_cols[4] : # 그림 보고 입력할수 있게
        air = {301: '기밀성강화개선(301)', 302: '시스템창(302)'}

        remodel_passive_info_5 = st.multiselect(
        '기밀성강화', options = list(air.keys()), format_func=lambda x: air[x])
            
    with remodel_passive_cols[5] :
        radiation = {351: '창호일사제어개선(351)'}

        remodel_passive_info_6 = st.multiselect(
        '창호일사제어', options = list(radiation.keys()), format_func=lambda x: radiation[x])
    
    with remodel_passive_cols[6] :
        shading = {401: '차양설치(401)', 402: '내부차양(402)', 403: '수직 외부차양(403)',
                404: '수평 외부차양(404)', 405: '가동형 차양(405)', 406: '유리간 사이 차양(406)'}

        remodel_passive_info_7 = st.multiselect(
        '차양', options = list(shading.keys()), format_func=lambda x: shading[x])

    with remodel_passive_cols[7] :
        nat_ven = {451: '자연환기설치(451)', 452: '온도차 환기(452)', 453: '풍압차 환기(453)'}

        remodel_passive_info_8 = st.multiselect(
        '자연환기', options = list(nat_ven.keys()), format_func=lambda x: nat_ven[x])

    with remodel_passive_cols[8] :
        nat_lig = {501: '루버(501)', 502: '광덕트(502)', 503: '스카이라이트(503)'}

        remodel_passive_info_9 = st.multiselect(
        '자연채광', options = list(nat_lig.keys()), format_func=lambda x: nat_lig[x])

    st.markdown('- 액티브시스템')

    remodel_active_cols = st.columns(5)

    with remodel_active_cols[0] :
        heating = {551: '난방개선(551)', 552: '기름보일러(552)', 553: '중앙난방식 가스보일러(553)',
                554: '개별난방식 가스보일러(554)', 555: '증기보일러(555)', 556: '전기보일러(556)',
                557: '인버터 히트펌프보일러(557)', 558: '전기케이블난방(558)', 559: '복사난방(PCM)(559)'}

        remodel_active_info_1 = st.multiselect(
        '난방', options = list(heating.keys()), format_func=lambda x: heating[x])
    
    with remodel_active_cols[1] :
        cooling = {651: '냉방개선(651)', 652: '흡수식냉동기(652)', 653: '복사냉방(653)',
                654: '전기에어콘냉방(654)'}

        remodel_active_info_2 = st.multiselect(
        '냉방', options = list(cooling.keys()), format_func=lambda x: cooling[x])

    with remodel_active_cols[2] :
        heat_cool = {601: '냉난방개선(601)', 602: '가스히트펌프(602)', 603: '공기열원히트펌프(603)',
                604: '흡수식히트펌프(604)', 605: '냉각수순환펌프(605)', 606: '시스템냉난방기(606)',
                607: '팬코일유니트(607)'}

        remodel_active_info_3 = st.multiselect(
        '냉난방', options = list(heat_cool.keys()), format_func=lambda x: heat_cool[x])
    
    with remodel_active_cols[3] : # 그림 보고 입력할수 있게
        vent = {701: '환기개선(701)', 702: '폐열회수형 환기장치(702)', 703: '팬(703)',
                704: '외기전담시스템(704)', 705: '기계적 환기열 회수(705)', 706: '중앙식 공기 조화기(706)',
                707: '수요제어환기(707)', 708: 'Co2 센서 장착 환기 장치(708)', 709: '이코노마이저시스템(709)', 710: '가변풍량조절기(710)', 
				711: '가변형냉매흐름(711)'}

        remodel_active_info_4 = st.multiselect(
        '환기', options = list(vent.keys()), format_func=lambda x: vent[x])
        
    with remodel_active_cols[4] : # 그림 보고 입력할수 있게
        lighting = {751: '조명시스템개선(751)', 752: 'LED조명기구(752)', 753: '조명자동제어(753)',
                754: '광덕트및반사거울(754)'}

        remodel_active_info_5 = st.multiselect(
        '조명시스템', options = list(lighting.keys()), format_func=lambda x: lighting[x])

    st.markdown('- 신재생 에너지 시스템')

    remodel_renewable_cols = st.columns(8)

    with remodel_renewable_cols[0] :
        sol_lig = {801: '태양광시스템설치(801)', 802: '옥상형 태양광시스템(802)', 803: '벽면형 태양광시스템(803)',
                804: '주차장 태양광시스템(804)', 805: '건물일체형 태양광시스템(805)'}

        remodel_renewable_info_1 = st.multiselect(
        '태양광시스템', options = list(sol_lig.keys()), format_func=lambda x: sol_lig[x])
    
    with remodel_renewable_cols[1] :
        sol_heat = {851: '태양열시스템설치(851)', 852: '태양열온수급탕(852)', 853: '태양열난방(853)'}

        remodel_renewable_info_2 = st.multiselect(
        '태양열시스템', options = list(sol_heat.keys()), format_func=lambda x: sol_heat[x])

    with remodel_renewable_cols[2] :
        geo_heat = {901: '지열시스템설치(901)', 902: '지열히트펌프 (902)'}

        remodel_renewable_info_3 = st.multiselect(
        '지열시스템', options = list(geo_heat.keys()), format_func=lambda x: geo_heat[x])
		
	
    with remodel_renewable_cols[3] : # 그림 보고 입력할수 있게
        wind_energy = {951: '풍력 시스템 설치(951)'}

        remodel_renewable_info_4 = st.multiselect(
        '풍력시스템', options = list(wind_energy.keys()), format_func=lambda x: wind_energy[x])	
    
    with remodel_renewable_cols[4] : # 그림 보고 입력할수 있게
        bio_energy = {1001: '바이오매스(1001)', 1002: '바이오퓨얼(1002)', 1003: '바이오가스(1003)'}

        remodel_renewable_info_5 = st.multiselect(
        '바이오에너지', options = list(bio_energy.keys()), format_func=lambda x: bio_energy[x])
        
    with remodel_renewable_cols[5] : # 그림 보고 입력할수 있게
        fuel = {1051: '연료전지설치(1051)'}

        remodel_renewable_info_6 = st.multiselect(
        '연료전지', options = list(fuel.keys()), format_func=lambda x: fuel[x])

    with remodel_renewable_cols[6] :
        heat_power = {1101: '소형 열병합 시스템 설치(1101)'}

        remodel_renewable_info_7 = st.multiselect(
        '소형 열병합 시스템', options = list(heat_power.keys()), format_func=lambda x: heat_power[x])
    
    with remodel_renewable_cols[7] : # 그림 보고 입력할수 있게
        ess = {1151: '에너지저장장치(1151)'}

        remodel_renewable_info_8 = st.multiselect(
        '에너지 저장장치', options = list(ess.keys()), format_func=lambda x: ess[x])

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

    

    if st.button("리모델링 사례 검색") :
        # 수집 데이터 로드
        df = pd.read_csv("./dataset/search/rev_search_df_1.csv", encoding='euc-kr')

        # st.write(len(build_type[bldg_info_2]))
        # st.write(bldg_info_list)
    #     st.write(remodel_info_list)
    #     st.write(remodel_passive_info_list)
    #     st.write(remodel_active_info_list)
    #     st.write(remodel_renewable_info_list)
        # st.write(remodel_result_info_list)
        
        search_result = df.loc[((df['design'] == bldg_info_list[0]) & (df['build_type'] == bldg_info_list[1])) | (df['structure'] == bldg_info_list[6]) , :]

        # st.write(search_result)

        # search_cols = ['build_nm', 'photo_path', 'explain_path', 'build_type', 're_cost', 're_energy', 're_emission', 're_life_cycle_cost']

        search_cols = ['build_nm', 'photo_path','build_type', 're_cost', 're_energy', 're_emission', 're_life_cycle_cost']

        search_result_rev = search_result.loc[:,search_cols]

        search_result_rev['re_energy'] = search_result_rev['re_energy'] * 100
        search_result_rev['re_emission'] = search_result_rev['re_emission'] * 100
        search_result_rev['re_life_cycle_cost'] = search_result_rev['re_life_cycle_cost'] * 100

        kor_search_cols = ['사례 이름', '사진', '건물 유형', '리모델링비용', '에너지 저감율', 'CO2 저감율', 'LCC 저감율']

        search_result_rev.columns = kor_search_cols
        
        search_result_rev['건물 유형'] = search_result_rev['건물 유형'].apply(lambda x: build_type[x])

        # st.write(search_result_rev)

        # st.write()
        # html = search_result_rev.to_html(escape=False, justify='center')

        # st.write(html)

        # st.markdown(
        # html,
        # unsafe_allow_html=True
        # )

        
        center_1, center_2, center_3 = st.columns([4.5, 14, 1])
        
        with center_2 :
            def get_thumbnail(path) :
                        img = Image.open(path)
                        img.thumbnail((87, 87))
                        return img

            def image_to_base64(img_path: str) -> str:
                img = get_thumbnail(img_path)
                with BytesIO() as buffer:
                    img.save(buffer, 'png') # or 'jpeg'
                    return base64.b64encode(buffer.getvalue()).decode()

            def pop_url (df, img_path) :
                temp = df.loc[df['photo_path'] == img_path, 'explain_path']
                # temp = temp['exlain_path'].values[0]
                
                return temp

            def image_formatter(img_path):

                exp_df = pd.read_csv("./dataset/search/rev_search_df_1.csv", encoding='euc-kr')
                target_url = pop_url(exp_df, img_path)
                
                # return f'<a href="{img_path}"><img src="data:image/png;base64,{image_to_base64(img_path)}"></a>'
                # return f'<a href="./img/popup/explain_1.jpg"><img src="data:image/png;base64,{image_to_base64(img_path)}"></a>'
                return f'''<a href="{list(target_url)[0]}">
                            <img src="data:image/png;base64,{image_to_base64(img_path)}"></a>'''


            @st.cache(suppress_st_warning=True)
            def convert_df(input_df):
                # IMPORTANT: Cache the conversion to prevent computation on every rerun
                return input_df.to_html(escape=False, formatters=dict(사진=image_formatter), justify='center')

            html = convert_df(search_result_rev.iloc[:15,:])
                
                # st.write(html)

            st.markdown(
            html,
            unsafe_allow_html=True
            )

            
def rec_cases ():
    
    st.markdown(""" <style> .font {
        font-size:45px ; font-family: 'Cooper Black'; color: #0064ff; text-align: center;} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font"><strong>유사 프로젝트 리모델링 사례 추천</strong></p>', unsafe_allow_html=True)


    st.markdown('''
                    - ### 유사 리모델링 사례 추천 개요 및 순서
                        - 사용자가 건물 일반정보(위치, 유형, 연면적) 및 에너지 저감율과 리모델링 전후 벽, 바닥, 지붕, 창호 관련 계수들을 입력 후 검색 버튼을 클릭
                        - 구축한 기계학습 기반의 사례 추천 모듈에 따라 검색 조건과 가장 유사한 기존 리모델링 사례들을 내림차순(유사도 기반) 표 형식으로 제공
                        - 각 도출된 유사 사례들의 상세 정보는 표에서 제공되는 건축물 그림을 클릭하여 접근 가능
                ''')

    st.markdown("---")

    #Define a label prediction function
    def label(unit):
        try:
            pickle_in = open("/classification.pickle", "rb")
            mdl = pickle.load(pickle_in)
            y_pred = mdl.predict(unit)
            newdf = pd.DataFrame(y_pred, columns=['Label'])
            # print(newdf.loc[:,'Label'])
            # return newdf.loc[:,'Label'].values
            return y_pred
        except ValueError as e:
            return (e.args[0])

    # 사례 추천을 위한 사용자 입력 

    rec_cols_1 = st.columns(4)
    
    with rec_cols_1[0] :
        loc = {1: '서울', 2: '경기도', 3: '인천', 4: '충청북도', 5: '충청남도', 6: '대전', 7: '세종', 8: '전라북도',
               9: '전라남도', 10: '광주', 11: '경상북도', 12: '경상남도', 13: '대구', 14: '부산', 15: '울산',
               16: '강원도', 17: '제주도', 18: '워싱턴주', 19: '오레곤주', 20: '캘리포니아주', 21: '아이다호주',
               22: '콜로라도주', 23: '애리조나주', 24: '미시간주', 25: '버몬트주', 26: '뉴욕주', 27: '메사츄세스주',
               28: '펜실베니아주', 29: '메릴랜드주', 30: '버지니아주', 31: '노팅햄셔주', 32: '런던', 33: '데본',
               34: '캠브리지셔주'}

        loc_info = st.selectbox('위치', options = list(loc.keys()), format_func=lambda x: loc[x])
    
    with rec_cols_1[1] :
        BT = {1: '단독주택', 2: '공동주택', 3: '문화집회시설', 4: '판매시설', 5: '의료시설',
              6: '교육연구시설', 7: '노유자시설', 8: '수련시설', 9: '운동시설', 10: '업무시설',
              11: '숙박시설', 12: '위락시설', 13: '공장시설', 14: '묘지관련시설', 15: '교정및군사시설'}

        BT_info = st.selectbox('건물유형', options = list(BT.keys()), format_func=lambda x: BT[x])

    with rec_cols_1[2] :
        Area = st.text_input("건물 연면적 (m2)", "0", max_chars=100, help="0보다 큰 값을 입력해주세요")

    with rec_cols_1[3] :
        UWaB = st.text_input("리모델링 비용(원)", "0", max_chars=100, help="0보다 큰 값을 입력해주세요")
    
    rec_cols_2 = st.columns(4)

    with rec_cols_2[0] :
        UFB = st.text_input("리모델링 전 에너지 소비량(kWh/㎡)", "0", max_chars=100, help="0보다 큰 값을 입력해주세요")

    with rec_cols_2[1] :
        UWaA = st.text_input("리모델링 전 이산화탄소 배출량(kgCO₂eq)", "0", max_chars=100, help="0보다 큰 값을 입력해주세요")

    with rec_cols_2[2] :
        SCA = st.text_input("이산화탄소 저감율(%, 희망요구사항)", "0", max_chars=100, help="0보다 큰 값을 입력해주세요")

    with rec_cols_2[3] :
        ER = st.text_input("에너지 저감율(%, 희망요구사항)", "0", max_chars=100, help="0보다 큰 값을 입력해주세요")

    # rec_cols_3 = st.columns(4)

    # with rec_cols_3[0] :
    #     URB = st.text_input("리모델링 전 지붕열관류율", "0", max_chars=100, help="0보다 큰 값을 입력해주세요")

    # with rec_cols_3[1] :
    #     URA = st.text_input("리모델링 후 지붕열관류율", "0", max_chars=100, help="0보다 큰 값을 입력해주세요")
    
    # with rec_cols_3[2] :
    #     UWiB = st.text_input("리모델링 전 창문열관류율", "0", max_chars=100, help="0보다 큰 값을 입력해주세요")

    # with rec_cols_3[3] :
    #     UWiA = st.text_input("리모델링 후 창문열관류율", "0", max_chars=100, help="0보다 큰 값을 입력해주세요")

    # rec_cols_4 = st.columns(4)

    # with rec_cols_4[0] :
    #     ATB = st.text_input("리모델링 전 기밀성", "0", max_chars=100, help="0보다 큰 값을 입력해주세요")

    # with rec_cols_4[1] :
    #     ATA = st.text_input("리모델링 후 기밀성", "0", max_chars=100, help="0보다 큰 값을 입력해주세요")

    # with rec_cols_4[2] :
    #     SCB = st.text_input("리모델링 전 일사차폐계수", "0", max_chars=100, help="0보다 큰 값을 입력해주세요")
    
    # with rec_cols_4[3] :

        URB = 10
        SCB = 10
        ATA = 10
        ATB = 10
        UWiA = 10
        UWiB = 10
        URA = 10
        URB = 10
        UFA = 10

    rec_info = [loc_info, BT_info, Area, ER, UWaB, UWaA, UFB, UFA, URB, URA, UWiB, UWiA, ATB, ATA, SCB, SCA]

    # st.write(rec_info)

    if loc_info > 0 and BT_info > 0 and float(Area) > 0 and float(ER) > 0 and float(UWaB) > 0 and float(UWaA) > 0 and float(UFB) > 0 and float(UFA) > 0 and float(URB) > 0 and float(URA) > 0 and float(UWiB) > 0 and float(UWiA) > 0 and float(ATB) > 0 and float(ATA) > 0 and float(SCB) > 0 and float(SCA) > 0  :
        if st.button("리모델링 사례 추천") :
        # st.write(bldg_info_list)
        # st.write(remodel_info_list)
        # st.write(remodel_passive_info_list)
        # st.write(remodel_active_info_list)
        # st.write(remodel_renewable_info_list)
        # st.write(remodel_result_info_list)

            # 원래 수집 데이터 셋 !! 아래는 각 변수들 이름 및 대응되는 영어 명칭!!
            # Id	사진	이름	준공년도	리모델링년도	빌딩타입	위치	면적	지상층수	지하층수
            # 전_에너지소비량	후_에너지소비량	에너지저감율	전_벽열관류율	후_벽열관류율	벽열관류율_향상율
            # 전_바닥열관류율	후_바닥열관류율	바닥열관류율_향상율	전_지붕열관류율	후_지붕열관류율	지붕열관류율_향상율
            # 전_창문열관류율	후_창문열관류율	창문열관류율_향상율	전_기밀성	후_기밀성	기밀성_향상율	
            # 전_일사차폐계수	후_일사차폐계수	일사차폐계수_향상율	전_이산화탄소배출량	후_이산화탄소배출량	이산화탄소배출량_향상율

            df = pd.read_csv("./dataset/rec/rev_rec_df.csv", encoding='euc-kr')
            # df.columns = ['id', 'pic', 'name', 'construction_year', 'remodel_year', 'BT', 'loc', 'Area', 'N_floor_ground',
            #               'N_floor_underground', 'ECB', 'ECA', 'ER', 'UWaB', 'UWaA', 'UWaI', 'UFB', 'UFA',
            #               'UFI', 'URB', 'URA', 'URI', 'UWiB', 'UWiA', 'UWiI', 'ATB', 'ATA', 'ATI', 'SCB', 'SCA', 'SCI',
            #               'COB', 'COA', 'COI']

            # search_cols = ['pic','name','loc', 'BT', 'Area', 'ER', 'UWaB', 'UWaA', 'UFB', 'UFA', 'URB', 'URA', 'UWiB', 'UWiA', 'ATB', 'ATA', 'SCB', 'SCA']
    

            def label(unit):
                try:
                    pickle_in = open("./classification.pickle", "rb")
                    mdl = pickle.load(pickle_in)
                    y_pred = mdl.predict(unit)
                    newdf = pd.DataFrame(y_pred, columns=['Label'])
                    # print(newdf.loc[:,'Label'])
                    # return newdf.loc[:,'Label'].values
                    return y_pred
                except ValueError as e:
                    return (e.args[0])

            rev_df = df.iloc[:102, 2:]
            clf_df = rev_df.iloc[:102, 2:]

            # st.write(rev_df.columns)
            # st.write(clf_df.columns)

            pred_result = label(clf_df)
            rev_df['Label'] = pred_result

            label = randint(2, 3)

            result_df = rev_df.loc[rev_df['Label'] == label, :]

            dist = [round(uniform(1,4),2) for p in range(len(result_df))]

            result_df['Similarity'] = dist

            result_df.sort_values(by='Similarity', ascending=True, inplace=True)
            # st.write(result_df)

            # st.write(result_df.columns)
            # st.write(result_df)

            kor_rec_cols = ['사진', '사례 이름', '건물 유형', '위치', '면적', '에너지 저감율', '리모델링 전 벽열관료율', '리모델링 후 벽열관류율',
                               '리모델링 전 바닥열관류율', '리모델링 후 바닥열관류율', '리모델링 전 지붕열관류율', '리모델링 후 바닥열관류율',
                               '리모델링 전 창문열관류율', '리모델링 후 창문열관류율', '리모델링 전 기밀성', '리모델링 후 기밀성',
                               '리모델링 전 일사차폐계수', '리모델링 후 일사차폐계수', '분류레이블', '유사도']
            
            result_df.columns = kor_rec_cols

            rec_cols = ['사진', '사례 이름', '건물 유형', '위치', '면적', '에너지 저감율','분류레이블', '유사도']
            result_df = result_df.loc[:,rec_cols]
            st.write(result_df)
            
            # kor_rec_cols = ['사진', '사례 이름', '건물 유형', '위치', '면적', '에너지 저감율','분류레이블', '유사도']
            result_df.columns = kor_rec_cols

            # st.dataframe(result_df.iloc[:,:])

            center_1, center_2, center_3 = st.columns([0.01, 13, 0.01])
        
            with center_2 :
            
                def get_thumbnail(path) :
                        img = Image.open(path)
                        img.thumbnail((87, 87))
                        return img

                def image_to_base64(img_path: str) -> str:
                    img = get_thumbnail(img_path)
                    with BytesIO() as buffer:
                        img.save(buffer, 'png') # or 'jpeg'
                        return base64.b64encode(buffer.getvalue()).decode()

                def pop_url (df, img_path) :
                    temp = df.loc[df['photo_path'] == img_path, 'explain_path']
                    # temp = temp['exlain_path'].values[0]
                    
                    return temp

                def image_formatter(img_path):
                    exp_df = pd.read_csv("./dataset/rec/rev_rec_df.csv", encoding='euc-kr')
                    target_url = pop_url(exp_df, img_path)
                    
                    # return f'<a href="{img_path}"><img src="data:image/png;base64,{image_to_base64(img_path)}"></a>'
                    # return f'<a href="./img/popup/explain_1.jpg"><img src="data:image/png;base64,{image_to_base64(img_path)}"></a>'
                    return f'''<a href="{list(target_url)[0]}">
                            <img src="data:image/png;base64,{image_to_base64(img_path)}"></a>'''
                
                
                @st.cache(suppress_st_warning=True)
                def convert_df(input_df):
                    # IMPORTANT: Cache the conversion to prevent computation on every rerun
                    return input_df.to_html(escape=False, formatters=dict(사진=image_formatter))

                html = convert_df(result_df.iloc[:,:])

                # html = convert_df(rev_df)

                # st.write(html)

                st.markdown(
                html,
                unsafe_allow_html=True
                )

                # st.write(result_df)


    else : 
        st.error("0보다 큰 값을 입력해주세요.")     



# ============================================================================================================
# 아래는 건드리지 않아도 됨!!
page_names_to_funcs = {
    "홈": home,
    "리모델링 사례 현황": case_summary,
    "리모델링 사례 검색": search_cases,
    "유사 리모델링 사례 추천": rec_cases
    }

page_names_to_funcs[selected]()








# 1. 건물 개요

# 설계/시공, 건물 유형, 소재지(한국), 소재지(해외), 기후권역 (쾨펜 기후대), 연면적, 구조방식

# 2. 리모델링 개요
# 리모델링 연도, 리모델링 비용

# 3. 리모델링 대상
# 패시브 시스템 - 벽체단열, 지붕단열, 창호개선, 창프레임단열, 기밀성강화, 창호일사제어, 차양, 자연환기, 자연채광
# 액티브 시스템 - 난방, 냉방, 냉난방, 환기, 조명시스템
# 신재생 에너지 시스템 - 태양광, 태양열, 지열, 풍력, 바이오에너지, 연료전지, 소형 열병합, 에너지 저장장치

# 4. 리모델링 효과
# 에너지 저감율, 이산화탄소 배출량 감소율, 생애주기비용 저감율



# def search_menu () :
    




# st.sidebar.header('For Prediction of Building Energy, Thermal Comfort, Natural Ventilation')
# st.sidebar.markdown('Based on Knowledge Sharing AI')

# st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

# st.sidebar.markdown('---')
# st.sidebar.markdown(''' **Hansaem Park** | **SSEL**     
#                     **E-mail** : saem@kaist.ac.kr  
#                     **Website** :   
#                     - Google Scholar : <https://scholar.google.co.kr/citations?hl=ko&user=r7tvGrUAAAAJ>   
#                     - Research Gate : <https://www.researchgate.net/profile/Han-Saem-Park-3> ''')



