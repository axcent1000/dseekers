

# 전환 효과
define flash = Fade(0.5, 0.0, 0.5, color="#fff")

# 게임에서 사용할 캐릭터를 정의합니다.
define f = Character('나레이션', color="#ffffff")
define e = Character('에이지', image = 'eiji', color="#5a61c1")
define loo = Character('루가몬', image = 'loo', color="#2730b4")
define tyranno = Character('티라노몬', image = 'tyranno', color="#ff0000")
define ryusenji = Character('류센지 교수', image = 'ryusenji', color="#919191")
define hina = Character('접수원', color="#53e0e8")
define hina2 = Character('하츠네', color="#53e0e8")
define leon = Character('레온 알렉산더', color="#bdd33f")
define pul = Character('펄스몬', color="#ddfc2a")
define hime = Character('사츠키', image = 'hime', color="#28bf80")

# 백그라운드 이미지
image background0 = "backgrounds/bg0.jpg" # 시작 화면
image bg_chap_f = "backgrounds/bg_chap_f.jpg" # 프롤로그
image bg_chap_1_1 = "backgrounds/bg_chap_1_1.png" # 챕터 1-1
image bg_chap_1_1_1 = "backgrounds/bg_chap_1_1_1.jpg"
image bg_chap_1_1_2 = "backgrounds/bg_chap_1_1_2.jpg"
image bg_chap_1_1_3 = "backgrounds/bg_chap_1_1_3.png"
image bg_chap_1_2 = "backgrounds/bg_chap_1_2.png" # 챕터 1-2
image bg_chap_1_2_1 = "backgrounds/bg_chap_1_2_1.png"
image bg_chap_1_2_2 = "backgrounds/bg_chap_1_2_2.png"
image bg_chap_1_2_3 = "backgrounds/bg_chap_1_2_3.jpg"
image bg_chap_1_2_4 = "backgrounds/bg_chap_1_2_4.jpg"
image bg_chap_1_2_5 = "backgrounds/bg_chap_1_2_5.png"
image bg_chap_1_2_6 = "backgrounds/bg_chap_1_2_6.jpg"
image bg_chap_1_3 = "backgrounds/bg_chap_1_3.png" # 챕터 1-3
image bg_chap_1_3_1 = "backgrounds/bg_chap_1_3_1.jpg"
image bg_chap_1_3_2 = "backgrounds/bg_chap_1_3_2.jpg"
image bg_chap_1_3_3 = "backgrounds/bg_chap_1_3_3.jpg"
image bg_chap_1_3_4 = "backgrounds/bg_chap_1_3_4.png"
image bg_chap_1_4 = "backgrounds/bg_chap_1_4.png" # 챕터 1-4
image bg_chap_1_4_1 = "backgrounds/bg_chap_1_4_1.png" 
image bg_chap_1_4_2 = "backgrounds/bg_chap_1_4_2.jpg"
image bg_chap_1_4_3 = "backgrounds/bg_chap_1_4_3.png"
image bg_chap_1_5 = "backgrounds/bg_chap_1_5.png" # 챕터 1-5
image bg_chap_1_5_1 = "backgrounds/bg_chap_1_5_1.jpg"
image bg_chap_1_5_2 = "backgrounds/bg_chap_1_5_2.jpg"
image bg_chap_1_5_3 = "backgrounds/bg_chap_1_5_3.jpg"
image bg_chap_1_5_4 = "backgrounds/bg_chap_1_5_4.jpg"
image bg_chap_1_5_5 = "backgrounds/bg_chap_1_5_5.png"
image bg_chap_1_5_6 = "backgrounds/bg_chap_1_5_6.png"
image bg_chap_1_5_7 = "backgrounds/bg_chap_1_5_7.png"
image bg_chap_1_5_8 = "backgrounds/bg_chap_1_5_8.png"
image bg_chap_1_5_9 = "backgrounds/bg_chap_1_5_9.png"
image bg_chap_1_5_10 = "backgrounds/bg_chap_1_5_10.jpg"
image bg_chap_1_5_11 = "backgrounds/bg_chap_1_5_11.jpg"
image bg_chap_1_5_12 = "backgrounds/bg_chap_1_5_12.png"
image bg_chap_1_6 = "backgrounds/bg_chap_1_6.png" # 챕터 1-6
image bg_chap_1_6_1 = "backgrounds/bg_chap_1_6_1.jpg"
image bg_chap_1_6_2 = "backgrounds/bg_chap_1_6_2.png"
image bg_chap_1_6_3 = "backgrounds/bg_chap_1_6_3.png"
image bg_chap_1_7 = "backgrounds/bg_chap_1_7.png" # 챕터 1-7
image bg_chap_1_8 = "backgrounds/bg_chap_1_8.png" # 챕터 1-8
image bg_chap_1_8_1 = "backgrounds/bg_chap_1_8_1.png"
image bg_chap_1_9 = "backgrounds/bg_chap_1_9.png" # 챕터 1-9
image bg_chap_1_9_1 = "backgrounds/bg_chap_1_9_1.png"
image bg_chap_1_9_4 = "backgrounds/bg_chap_1_9_4.png"


# 소속 로고 이미지
image fang = "characters/fang.png" # 팡
image dd = "characters/dd.png" # 디지대
image jj = "characters/jj.png" # 해커 저지
image soc = "characters/soc.png" # 크래커 그룹 SoC

# 아이템
image gadget = im.FactorScale("characters/gadget.png", 0.6)
image dmap = im.FactorScale("characters/dmap.png", 0.65)
image devo = im.FactorScale("characters/devo.png", 0.65)
image obj = im.FactorScale("characters/obj.png", 0.65)
image digitama = im.FactorScale("characters/digitama.png", 0.65)
image lighting = im.FactorScale("characters/lighting.png", 1.5)
image lighting2 = im.FactorScale("characters/lighting2.png", 1.0)
image loo_windows = im.FactorScale("characters/loo_windows.png", 0.6)
image loo_windows2 = im.FactorScale("characters/loo_windows2.png", 0.6)
image loo_windows3 = im.FactorScale("characters/loo_windows3.png", 0.6)
image loo_windows4 = im.FactorScale("characters/loo_windows4.png", 0.6)
image loo_windows5 = im.FactorScale("characters/loo_windows5.png", 0.6)
image hacktv = im.FactorScale("characters/hacktv.png", 0.6)

# 인간 캐릭터 이미지
image eiji = im.FactorScale("characters/e.png", 0.7)
image side eiji nomal = "characters/e_side_nomal.png"

image ryusenji = im.FactorScale("characters/ryusenji.png", 1.2)
image side ryusenji nomal = "characters/ryusenji_side_nomal.png"


image hina = im.FactorScale("characters/hina.png", 1.5) # 접수원 하츠네

image hime = im.FactorScale("characters/hime.png", 1.2) # 타마히메 사츠키
image side hime nomal = im.FactorScale("characters/hime_side_nomal.png", 1.0) # 타마히메 사츠키

image dd2 = "characters/dd2.png" # 디지대 2번 여자

image leon = "characters/leon.png" # 레온 알렉산더

# 디지몬 캐릭터 이미지
image loo = im.FactorScale("characters/loo.png",0.65) # 루가몬
image tyranno = im.FactorScale("characters/tyranno.png", 2.0) # 티라노몬
image pul = "characters/pul.png" # 펄스몬 


# 여기에서부터 게임이 시작합니다.
label start:
    scene bg_chap_f with fade
    stop music

#챕터 선택 분기
    menu:

        "시작할 챕터를 선택해주세요."
        "프롤로그":
            jump Chapter_P
        
        "Chapter 1":
            menu:
                "시작할 챕터를 선택해주세요."
                "Chapter 1-1":
                    jump Chapter1_1
                "Chapter 1-2":
                    jump Chapter1_2
                "Chapter 1-3":
                    jump Chapter1_3
                "Chapter 1-4":
                    jump Chapter1_4
                "Chapter 1-5":
                    jump Chapter1_5
                "다음 페이지":
                    
                    menu:
                        "시작할 챕터를 선택해주세요."
                        "Chapter 1-6":
                            jump Chapter1_6
                        "Chapter 1-7":
                            jump Chapter1_7
                        "Chapter 1-8":
                            jump Chapter1_8
                        "Chapter 1-9":
                            jump Chapter1_9
                    #     "Chapter 1-10":
                    #         jump Chapter1_4

# 프롤로그 진행
label Chapter_P:

    scene black with blinds
    scene bg_chap_f with fade
    play music "audio/bgm/bgm1.mp3" fadein 0.5

    f "인류의 현실 세계와는 다른 「디지털 월드」"
    
    f "――이 네트워크상의 전뇌공간에 서식하는 것이 디지털 몬스터"
    
    f "통칭「디지몬」이다."

    f "AI 생명체 디지몬의 발견은 모든 것이 네트워크로 관리되는 인간 사회에, 빛과 그림자를 드리우고 있었다."

    show eiji with dissolve
    f "「나가스미 에이지」는 디지털 세계와 관련된 위험한 일로 돈을 버는 19살 하류인생 크래커이다.."

    f "어느 날 에이지는 도쿄 전뇌 대학의 권위자인 류센지 교수의 초대를 받아 최신 디지몬 독 「디지몬 링커」와
    함께 어떤 디지몬을 만나게 된다."

    show eiji at Position(xalign = 0.35, yalign = 1.0) with move
    show loo at Position(xalign = 0.75, yalign = 0.6) with dissolve
    f "이마에 수수께끼의 인터페이스를 장착한 늑대형 디지몬 「루가몬」과의 만남은
    에이지의 일상을 완전히 바꿔 놓는다."

    scene bg_chap_f with dissolve

    show jj at Position(yalign = 0.45) with fade
    f "크래커를 증오하는 정의의 해커 「판사」"
    hide jj with dissolve
    
    show dd at Position(yalign = 0.45) with fade
    f "디지몬 범죄에 대응하는 경시청 사이버범죄과 수사 제11계 「디지대」"
    hide dd with dissolve

    show soc at Position(yalign = 0.45) with fade
    f "전설의 크래커 타르타로스가 이끄는 무투파 크랙팀 「SoC」(Sons of Chaos) ......."
    hide soc with dissolve

    with fade

    f "에이지가 류센지의 의뢰로 SoC에 잠입 조사를 하려고 한다."

    f "SoC에 의해 대규모 사이버 테러가 계획되고 있었던 것이다."
    
    f "소중한 스킬 - 마인드 링크는 무엇일까?"

    f "잃어버린 루가몬의 과거와 진정한 스펙은?"

    f "에이지가 디지털 월드에서 승리하고 궁극의 인생 역전을 이룰 수 있을까 ......?"
    stop music fadeout 0.5
    with fade

    $ renpy.movie_cutscene("/audio/video/video1.webm")

# 챕터 1-1 시작
label Chapter1_1:

    scene black with blinds
    scene bg_chap_1_1 with blinds

    voice "audio/voice/v1.mp3"
    "Chapter1-1" "Eiji: Wolf of ninth avenue" 
    
    scene bg_chap_1_1_1 with fade
    voice "audio/voice/v2.mp3" 
    f "와이어 프레임으로 된 T-REX가 달린다."

    voice "audio/voice/v3.mp3"
    f "티라노사우루스 렉스."

    voice "audio/voice/v4.mp3"
    f "약 6700만년 전, 백악기의 대지에 군림했던 육식 파충류다. 최대급으로 체장 13미터, 중량 9톤."

    voice "audio/voice/v5.mp3"
    f "공룡."

    voice "audio/voice/v6.mp3"
    f "하지만, 그것은 화석을 근거로 한 학자의 상상화와는 조금 달랐다."

    voice "audio/voice/v7.mp3"
    f "T-REX보다도 훨씬 작다."

    voice "audio/voice/v8.mp3"
    f "그러면서도 앞다리는 유달리 발달해 있으며, 날카로운 3개의 갈고리 발톱은 사냥감의 살을 확실히 발라낼 수 있을 것이다."

    scene bg_chap_1_1_3 with fade
    voice "audio/voice/v9.mp3"
    f "――티라노몬 성숙기  공룡형  데이터종"

    scene bg_chap_1_1_1 with fade
    voice "audio/voice/v10.mp3"
    f "와이어 프레임의 3D 몸체에 피부 텍스쳐가 입혀져 가며, 매핑―― 질감이 생겨 간다."

    voice "audio/voice/v11.mp3"
    f "빨간 T-REX 비슷한 것이 달린다."

    voice "audio/voice/v12.mp3"
    f "그들은 무리를 짓고 있었다."

    voice "audio/voice/v13.mp3"
    f "1마리가 사냥감을 쫓고, 1마리는 꾀어내고, 또 1마리는 매복…… 고도의 지능에 기반하여 집단을 이룬 사냥을."

    voice "audio/voice/v14.mp3"
    f "사냥감은 몰아붙여지고 있다."

    voice "audio/voice/v15.mp3"
    f "터널 안쪽으로, 더 안쪽으로."

    voice "audio/voice/v16.mp3"
    f "덮쳐오는 티라노몬의 갈고리 발톱이, 드디어 사냥감을 붙잡으려고 한 순간,"
    
    with fade

    voice "audio/voice/v17.mp3"
    "빠앙――――" with vpunch

    voice "audio/voice/v18.mp3"
    f "구오오오오오오오…… 귀를 찢는 굉음과 함께, 사각형의 거대한 물체가 맹렬한 스피드로 스쳐 지나갔다."

    voice "audio/voice/v19.mp3"
    f "지하철이다."

    voice "audio/voice/v20.mp3"
    f "와이어 프레임으로 그려진 열차―― 순간적으로 열차를 피한 티라노몬이 바라보고 있는 범위만은, 노선을 가리키는 라인 컬러의 버밀리온(주홍색)으로 칠해져 있었다."

    voice "audio/voice/v21.mp3"
    f "행선지 표시에는 어딘가에서 본 것 같으면서도, 무슨 언어인지 알 수 없는 불가해한 문자의 나열이."

    voice "audio/voice/v22.mp3"
    f "그곳은 태곳적의 정글이 아닌, 선화로 구축된 콘크리트 지하 공간."

    voice "audio/voice/v23.mp3"
    f "３마리의 티라노몬은 다시 도망친 사냥감을 쫓아간다."

    voice "audio/voice/v24.mp3"
    f "터널 내의 갈림길에서 꺾어 더욱 지하 깊은 곳으로."

    voice "audio/voice/v25.mp3"
    "첨벙"

    voice "audio/voice/v26.mp3"
    f "물을 밟는 소리."

    voice "audio/voice/v27.mp3"
    f "그 앞은 광대한 하수도로 이어져 있었다."

    voice "audio/voice/v28.mp3"
    f "주위는 뻗은 손가락의 끝조차 보이지 않는 어둠으로."

    voice "audio/voice/v29.mp3"
    f "하지만, 티라노몬은 지각하고 있다."

    voice "audio/voice/v30.mp3"
    f "불어오는 바람이 가져온 오물 냄새, 재빠르게 수로를 도망치고 있는 사냥감의 발소리…… 즉 공기를."

    with fade

    voice "audio/voice/v31.mp3"
    tyranno "갸악!!!" with vpunch

    voice "audio/voice/v32.mp3" 
    f "매복 역할의 티라노몬이 비명을 질렀다."

    voice "audio/voice/v33.mp3"
    f "갑자기 회오리가 발생하여, 말려 올라간 물 기둥 소용돌이가 티라노몬을 날려버렸다."

    voice "audio/voice/v34.mp3"
    f "균형을 잃은 티라노몬은 등쪽부터 수로로 쓰러져, 배를 드러내고 뒤집어지고 만다."

    voice "audio/voice/v35.mp3"
    "?" "슈아아아아아" with vpunch

    voice "audio/voice/v36.mp3"
    f "거기에 지근거리에서 추격 충격파, 기습으로 강렬한 마무리 일격을 가했다."

    voice "audio/voice/v37.mp3"
    f "사냥감에 반격당한 티라노몬은 침묵, 빨간 피부에 ―― 노이즈가 퍼져간다."
    
    scene black with blinds
    scene bg_chap_1_1_2 with blinds

    voice "audio/voice/v38.mp3"
    f "튀어나오는 간판―― 3D 디지털 사이니지(전자간판) 광고."

    voice "audio/voice/v39.mp3"
    f "얼굴에 쿠마도리(가부키 분장의 일종) 화장을 한 괴상한 가부키 풍 샵 마스코트가, 
    가게에서 도로로 튀어나갈 것 같은 기세로 새로 발매된 어쩌고 고기 4배 버거를 선전하고 있다."

    voice "audio/voice/v40.mp3"
    e nomal "뭔가, 좋은 알바 이야기 없으려나~"

    voice "audio/voice/v41.mp3"
    f "나가스미 에이지는 패스트푸드점의 2층 구석 자리에 자리를 잡고 쿠폰으로 받은 드링크로 죽치고 있었다."

    voice "audio/voice/v42.mp3"
    f "스마트폰을 한 손에 들고 SNS―― GriMM(그림)의 토픽을 흐르듯이 읽고 있다."

    voice "audio/voice/v43.mp3"
    f "GriMM은 범세계적 커뮤니케이션 툴이다."

    voice "audio/voice/v44.mp3"
    f "기본 기능인 짧은 메시지, 보이스 채팅, 영상, 라이브 방송 기능 외에, 기룹 채널에 기반한 다양한 커뮤니티가 병립하고 있다."

    voice "audio/voice/v45.mp3"
    f "총 유저수는 모든 SNS 중에서도 아마도 상위. 최대 특징은, 독자적인 암호 화폐 DC(디지코인)에 의한 금융 결제 툴을 겸하고 있어 하나의 경제권을 이루고 있다는 점이다."
    
    voice "audio/voice/v46.mp3"
    f "단, 반쯤은, 비합법이다."

    voice "audio/voice/v47.mp3"
    e "툴의 코스트가 만만치가 않으니 외주로 맡길 게 아니라 프로그램 같은 거 진심으로 배워야겠는데-. 어라…… 칩 가격 또 올랐냐고. 우리 업계도 드디어 레드 오션인가-"

    voice "audio/voice/v48.mp3"
    f "그럴싸한 말을 혼자서 주워섬긴다."

    voice "audio/voice/v49.mp3"
    f "정보 수집, 개인 매매, 클라우드 소싱의 장으로서, GriMM은 에이지 같은 프리터에게 있어서 돈 버는 데에 필수다."

    voice "audio/voice/v50.mp3"
    f "GriMM은 말하자면, 새로운 가치관에 근거한 네트워크상의 공화국인 것이다."

    voice "audio/voice/v51.mp3"
    f "……라고 해도 과장은 아닐 것이다. 그 경제 규모는 지금은 현실의 대국을 위협할 정도인 것이다."

    voice "audio/voice/v52.mp3"
    e "성장 브리더…… 는 허들이 높지. 역시 콜렉터를 상대로 한 포획이 손쉽게 벌 수 있나."

    voice "audio/voice/v53.mp3"
    e "하지만 전업 헌터가 될 거라면 고객 상대로 판매 루트를 만들지 않으면……" 

    voice "audio/voice/v54.mp3"
    e "... 검은 아구몬?"

    voice "audio/voice/v55.mp3"
    e "포획 보수 1억 DC?!" with vpunch

    voice "audio/voice/v56.mp3"
    f "에이지는, 어떤 모집에 달려들었다."

    voice "audio/voice/v57.mp3"
    f "「아구몬」이란, GriMM에 드나드는 에이지 같은 크래커―― 네트워크 비정규 노동자 일대에서 취급되는 데이터의 일종, 그 이름이다."

    voice "audio/voice/v58.mp3"
    f "――「아구몬・검정」 「상처 없이 살아있는 것에 한정」"

    voice "audio/voice/v59.mp3"
    f "공룡형 실루엣에 모집 내용과 주의사항이 정리되어 있었다."

    voice "audio/voice/v60.mp3"
    f "1억 DC라고 하면, 대략 1억엔 이상……?"

    voice "audio/voice/v61.mp3"
    f "에이지는 상상도 할 수 없는 거금이지만, 10년 이상은 일하지 않고 살 수 있을 것이리라."

    voice "audio/voice/v62.mp3"
    f "하지만, 본문에 달린 리플들을 바라본 에이지는, 바로 텐션이 떨어졌다."

    voice "audio/voice/v63.mp3"
    f "이것도 저것도 욕설이나 장난 목적, 돈을 요구하기만 할 뿐인 발언뿐……"

    voice "audio/voice/v64.mp3"
    f "GriMM은 무법지대인 것이다. 네트워크의 쓰레기장이다."
    
    voice "audio/voice/v65.mp3"
    e "아-, 이거 유명한 도시전설 소재인가. 1억이라니 비현실적이고, 애당초 검은색이면 아구몬이 아니잖아……"

    voice "audio/voice/v66.mp3"
    e "엣, 아악-!! 내 티라노몬 3호가아!" with vpunch

    voice "audio/voice/v67.mp3"
    f "자기도 모르게 목소리가 나왔다."

    voice "audio/voice/v68.mp3"
    f "같은 층에 있던 고등학생 몇 명 그룹이, 힐끔 에이지를 봤다."

    voice "audio/voice/v69.mp3"
    f "작년까지는――"

    voice "audio/voice/v70.mp3"
    f "에이지도 그들처럼 고등학교 교복을 입고 있었다."

    voice "audio/voice/v71.mp3"
    f "저런 식으로 잡담이나 하며, 목표도 없이, 그 대신에 장래에 대한 불안도 없는, 그다지 실감도 없는 즐거운 매일을……"

    voice "audio/voice/v72.mp3"
    f "스마트폰을 스와이프 하는 손을 멈추고, 다른 쪽 손으로 테이블에 놔둔 가젯을 만졌다."

    show gadget at Position(xalign = 0.5,yalign = 0.35) with dissolve
    voice "audio/voice/v73.mp3"
    f "손바닥 사이즈로, 흑백 액정 화면과 조작 버튼이 달려 있다. 언뜻 보면 전자 토이―― 장난감 같다."

    voice "audio/voice/v74.mp3"
    f "화면에는 소위 말하는 도트 그림으로, 데포르메된 공룡 같은 것이 비춰지고 있었다."

    voice "audio/voice/v75.mp3"
    f "――티라노몬"

    voice "audio/voice/v76.mp3"
    f "이름이 표시된다. 하지만, 그 눈은 ×자가 되어서 다운되어 있었다."

    hide gadget with dissolve
 
    voice "audio/voice/v77.mp3"
    e "알바 찾는데 집중하느라 알바비가 날아가 버렸다~." 

    voice "audio/voice/v78.mp3"
    e "바보바보, 나 바보!" with vpunch

    voice "audio/voice/v79.mp3"
    f "에이지는 자기 머리를 퍽퍽 때렸다."

    voice "audio/voice/v80.mp3"
    f "다른 2마리―― 티라노몬 1호와 2호가, 작은 흑백 화면에서 번갈아가며 에이지 쪽을 봤다."

    voice "audio/voice/v81.mp3"
    f "곤란해 하는 것 같으며, 마치 지시를 기다리고 있는 것처럼."

    voice "audio/voice/v82.mp3"
    e "부탁한다고! 이 이상은 적자가 난단 말야……!"

    voice "audio/voice/v83.mp3"
    f "에이지는 가젯을 조작하며 다운된 티라노몬을 다른 개체로 바꾸었다."

    voice "audio/voice/v84.mp3"
    e "――타겟을 포획하지 못하면 너희들 밥 없어! 그보다 포획하지 못하면 내가 이번 달 반찬 없이 먹어야 한다고"

    voice "audio/voice/v85.mp3"
    f "게임에 흥분하고 있는 위험한 녀석이라고 여겨진 것 같다."

    voice "audio/voice/v86.mp3"
    f "고등학생들은 눈썹을 찡그리며 자리에서 이동해 버렸다."

    voice "audio/voice/v87.mp3"
    f "하지만, 이것은 게임이 아니다."

    voice "audio/voice/v88.mp3"
    f "놀이가 아니다."

    voice "audio/voice/v89.mp3"
    f "에이지는 크래커다."

    voice "audio/voice/v90.mp3"
    f "컴퓨터에 관한 탁월한 기술을 가진 인간을 해커라고 부르나, 크래커는, 해커 중에서도 「비합법」"

    voice "audio/voice/v91.mp3"
    f "「그레이 존」의 활동을 마다치 않는 네트워크 업계의 청부업자다."

    voice "audio/voice/v92.mp3"
    e "툴 설정「포획」! 타겟 재지정 「투베타몬 !」크래커「팽」나가스미 에이지를 얕보지 말라고…… 커맨드 실행! ＆방치!"

    voice "audio/voice/v93.mp3"
    f "꾹 하고 실행 버튼을 눌렀다."

    voice "audio/voice/v94.mp3"
    f "흑백 액정 화면의 티라노몬들이 어딘가로 사라져 간다."

    voice "audio/voice/v95.mp3"
    f "일하러 나간 것이다. 이 다음은 AI가 사전에 툴에 지정해둔 대로 「사냥감」을 포획해 올 것이다."

    voice "audio/voice/v96.mp3"
    f "물기에 불은 종이컵의 드링크를 들이키고, 에이지는 다시 GriMM을 넘겨보기 시작했다."

    "Chapter 1-1 End..." with Pause(20)
# 챕터 1-2 시작
label Chapter1_2:   

    scene black with blinds
    scene bg_chap_1_2 with blinds

    voice "audio/voice/v1.mp3"
    "Chapter1-2" "Eiji: Wolf of ninth avenue" 

    voice "audio/voice/v97.mp3"
    f "도쿄 전뇌 대학은, 이학 기술과 나라의 미래를 짊어지는 이과계 학생을 우대・서포트하는 정부의 핵심 정책으로서 설립되었다."
    
    voice "audio/voice/v98.mp3"
    f "역사는 짧지만, 정보 공학 분야에서 톱 클래스의 연구와 실적을 자랑한다."

    voice "audio/voice/v99.mp3"
    f "다국적 도시 도쿄의 새로운 중심이 된 덴린(電臨)구라는 입지."

    voice "audio/voice/v100.mp3"
    f "글로벌 기업, 소위 말하는 빅 테크 기업의 취직에 강하다는 평가도 있어서 점점 수험생에게서 인기가 높아지고 있다."

    voice "audio/voice/v101.mp3"
    f "그 전뇌대 덴린 캠퍼스에 인접한 곳에, 한가지 더 시설이 있었다."

    scene bg_chap_1_2_1 with fade
    voice "audio/voice/v102.mp3"
    f "어바딘 일렉트로닉스(Abadin Electronics Corp. AE)."

    voice "audio/voice/v103.mp3"
    f "전자단말, 네트워크 기기, 패브래스(무설비) 반도체 등에 손을 뻗고 있는 톱 기업이다."

    voice "audio/voice/v104.mp3"
    f "어바딘 일렉트로닉스 덴린구 디지털 라보―― 통징 DDL은, AE사의 연구 개발 거점이었다."

    voice "audio/voice/v105.mp3"
    f "DDL의 1층 로비는, 에이지가 상상했던 것보다도 심플했다."

    voice "audio/voice/v106.mp3"    
    f "접수처, 흔해 빠진 대기자용 벤치."

    voice "audio/voice/v107.mp3"
    f "벽면의 대형 디스플레이에서는 AE사의 선전을 하고 있는 것도 아니고……"

    voice "audio/voice/v108.mp3"
    f "대초원, 밀림, 극해(極海), 대산맥, 단풍이 든 계곡, 지저 동굴……"

    voice "audio/voice/v109.mp3"
    f "그러한 사시사철의 자연이 짜내는 환경 영상이, 그저 틀어지고 있었다."

    voice "audio/voice/v110.mp3"
    e nomal "디지털 라보는 연구 시설이니까…… AE사의 본사는 바깥이고"

    voice "audio/voice/v111.mp3"
    f "완만한 곡면으로 구성된 라보의 외벽은 녹화(緑化)되어 있어, 회사의 로고, 그거라고 알 법한 간판 같은 것도 없다."

    voice "audio/voice/v112.mp3"
    f "지나가는 사람은 옆에 있는 전뇌대의 건물이라고 생각할지도 모른다."

    voice "audio/voice/v113.mp3"
    show eiji with dissolve
    f "에이지는 유리에 비친 자기 모습을 보았다."

    voice "audio/voice/v114.mp3"
    f "평소와 같은 러프한 복장이다. DDL에서의 근무는 캐주얼 웨어가 가능하다고는 하지만."

    voice "audio/voice/v115.mp3"
    f "여기서 일하고 있는 것은 선발된 우수한 두뇌를 가진 엘리트뿐일 터이다."

    voice "audio/voice/v116.mp3"
    f "고졸 프리터가 있을 자리는 아니다."

    voice "audio/voice/v117.mp3"
    f "하지만 에이지는 주눅들지 않고 접수처로 걸어갔다."

    voice "audio/voice/v118.mp3"
    f "그렇다, 일이니까."

    scene black with blinds
    scene bg_chap_1_2_2 with blinds

    voice "audio/voice/v119.mp3"
    e nomal "안녕하세요-"

    voice "audio/voice/v120.mp3"
    f "에이지는 애교 있는 태도로 말을 걸었다. 접수처의 그녀에게."

    show hina at Position(xalign = 0.5,yalign = -0.15) with dissolve
    voice "audio/voice/v121.mp3"
    hina "네?"
    
    voice "audio/voice/v122.mp3"
    f "뭐지, 이 수상한 젊은이는……? 라고 말하는 듯한 느낌의 시선이 돌아왔다."

    voice "audio/voice/v123.mp3"
    f "사각형 가방을 메고 있지 않으니 음식 배달을 온 게 아니라는 건 알 수 있을 것이다."

    voice "audio/voice/v124.mp3"
    f "아아, 그런가…… 아마, 실수로 라보에 들어와 버린 대학생이나 지나가던 사람이 가끔 있는 것이다. 그런 부류라고 생각한 것이리라."

    voice "audio/voice/v125.mp3"
    e "약속이 잡혀 있는데. 이 태블릿에 적으면 될까?"

    voice "audio/voice/v126.mp3"
    f "연구시설쯤 되면 기업의 비밀을 안고 있다."

    voice "audio/voice/v127.mp3"
    f "저편에 있는 게이트에는 건장한 가드맨이 몇 명 모여 있었다."

    voice "audio/voice/v128.mp3"
    f "여기가 미국이었다면 권총 정도는 가지고 있을 법한 삼엄한 분위기다."

    voice "audio/voice/v129.mp3"
    hina "네…… 그러시면……"

    voice "audio/voice/v130.mp3"
    f "망설이는 목소리도 귀엽다."

    voice "audio/voice/v131.mp3"
    f "목덜미 부근에서 폭이 좁아지는 볼륨 있는 숏컷 헤어."

    voice "audio/voice/v132.mp3"
    f "연구소다운 수수한 사무원 스타일이지만, 얼굴이 작고, 목과 어깨가 가늘어, 아무튼 가만히 있기만 해도 인기 있겠구나 싶은 느낌이다."

    voice "audio/voice/v133.mp3"
    e "――성명칸에는 본명? 나, 일할 때는 다른 이름을 쓰고 있는데"

    voice "audio/voice/v134.mp3"
    hina "실례지만 예능계나 작가 분이신가요?"

    voice "audio/voice/v135.mp3"
    e "아-니"

    voice "audio/voice/v136.mp3"
    f "예명이나 펜네임은 아니다. 에이지는, 대다수의 크래커가 그러하듯이, 일할 때에는 통칭인 크래커 네임을 쓰고 있다."

    voice "audio/voice/v137.mp3"
    hina "문제가 없으시다면... 본명으로"

    voice "audio/voice/v138.mp3"
    e "나가스미 에이지……. 전화번호, 약속 시간…… 용건은 상담 같은 거면 될까? 하츠네쨩"

    voice "audio/voice/v139.mp3"
    f "에이지는 상대의 이름표를 보고 있었다."

    voice "audio/voice/v140.mp3"
    hina2 "갑자기 쨩 붙여서 부르는 건 그만둬주세요"

    voice "audio/voice/v141.mp3"
    e "그럼, 하츠넷치"

    voice "audio/voice/v142.mp3"
    f "…………!  접수원 하츠네는, 관자놀이 부근을 움찔거렸다." 
    
    voice "audio/voice/v143.mp3"
    hina2 "상담이시라면, 이쪽에 귀사의……"

    voice "audio/voice/v144.mp3"
    e "아직 회사를 차린 건 아닌데-"
 
    voice "audio/voice/v145.mp3"
    hina2 "하아"

    voice "audio/voice/v146.mp3"
    e "에- 어디, 내 직업은…… 그러고 보니 그 사람의 부서는 뭐였더라? 아아, 진짜, 귀찮구만-"

    voice "audio/voice/v147.mp3"
    f "에이지는 스마트폰을 손에 들었다."

    scene black with fade

    show ryusenji at Position(xalign = 0.5,yalign = -0.2) with dissolve
    voice "audio/voice/v148.mp3"
    f "――류센지 토모노리(교수)"

    # 메세지 보내기 작업 필요
    #
    #
    
    scene bg_chap_1_2_1 with fade
    voice "audio/voice/v149.mp3"
    f "주소를 탭하고 「도착했어요」라고 메시지를 보내자, 로비에서 기다리기로 했다."

    voice "audio/voice/v150.mp3"
    f "다른 방문객은 몇 명. 접수처에서 게스트 패스를 받고 있다."

    voice "audio/voice/v151.mp3"
    f "모두 영업 비즈니스맨이라고 하기 보다는 그야말로 전뇌대에 있을 법한 아카데믹한 분위기를 두르고 있었다."

    voice "audio/voice/v152.mp3"
    e nomal "(…………)"

    voice "audio/voice/v153.mp3"
    f "에이지는 문득 로비 중앙의 오브제에 눈길을 줬다."

    voice "audio/voice/v154.mp3"
    f "3개의 구체가 공중에 떠 있었다."

    voice "audio/voice/v155.mp3"
    f "구체에는 각각 특징적인 마크가 새겨져 있다."

    voice "audio/voice/v156.mp3"
    f "미츠도모에(三つ巴)―― 라고 하던가. 그것들은, 서로 겹쳐지면서 회전하고 있었다."

    voice "audio/voice/v157.mp3"
    f "흡사 우주 공간에서 서로의 중력에 이끌리고 있는 3개의 구상성단."

    voice "audio/voice/v158.mp3"
    e "(그보다, 이런 게 방금 전까지 있었던가……?)"

    voice "audio/voice/v159.mp3"
    f "가까이 다가가고 나서, 에이지는 놀랐다."

    voice "audio/voice/v160.mp3"
    e "이거 입체영상……「홀로라이즈」인가!"

    voice "audio/voice/v161.mp3"
    "?" "――여어, 「팽」!"

    voice "audio/voice/v162.mp3"
    f "게이트 너머에서, 크래커 네임으로 부르는 목소리가 날아들었다."

    voice "audio/voice/v163.mp3"
    f "그와 동시에, 미츠도모에의 오브젝트는 무너지면서 흔적도 없이 사라진다."

    voice "audio/voice/v164.mp3"
    f "에이지는 돌아봤다."

    scene bg_chap_1_2_3 with fade

    voice "audio/voice/v165.mp3"
    f "키는 170센치 정도. 이목구비가 뚜렷한 로맨스 그레이의 머리칼, 약간 백인 같은 분위기도 있었다." 
    
    voice "audio/voice/v166.mp3"
    f "연령은 60대 정도일 터이나, 발걸음이나 자세도 좋아 훨씬 젊게 보였다."
    
    voice "audio/voice/v167.mp3"
    f "그 존재감은, 그 본인보다도 주변의 반응을 보는 편이 알기 쉽다."

    voice "audio/voice/v168.mp3"
    f "로비에 있던 전원이 뜻밖에 나타난 그에게 주목한 것이었다."

    voice "audio/voice/v169.mp3"
    e nomal "안녕하세요, 류센지…… 교수님!"

    voice "audio/voice/v170.mp3"
    f "어바딘 일렉트로닉스의 공통 설립자 중 한 사람."

    voice "audio/voice/v171.mp3"
    f "대부호다. 시가 총액 1000억 달러를 넘는 AE사의 주식을, 아직도 20퍼센트 넘게 소유하고 있다."

    voice "audio/voice/v172.mp3"
    f "교수, 라는 것은 그는 대학 교수이기도 하기 때문이다."

    voice "audio/voice/v173.mp3"
    f "업계에서는 잘 알려진 류센지 연구실의 보스로서 현재는 전뇌대 명예 교수."

    voice "audio/voice/v174.mp3"
    f "한때 대학에서 세워진 벤처로서 일어난 그의 기업을 최고 간부의 한 사람으로서 10년, 20년 만에 현재의 세계적 기업으로 길러내었다."

    voice "audio/voice/v175.mp3"
    ryusenji "크래커 팽으로서 만나는 건 처음이다만, 그런 느낌은 안 드는군"

    voice "audio/voice/v176.mp3"
    f "구름 위의 사람, 이라고 해야 할 것이리라."

    voice "audio/voice/v177.mp3"
    f "평범하게 생각하면 류센지는 에이지가 편하게 접할 수 있는 입장의 사람은 아니다."

    scene bg_chap_1_2_2 with fade

    voice "audio/voice/v178.mp3"
    e nomal "항상 보이스 채팅으로 이야기하고 있으니까 말이죠. 아, 나가스미 에이지입니다"

    voice "audio/voice/v179.mp3"
    f "에이지는 새로이 자기소개를 했다."

    voice "audio/voice/v180.mp3"
    ryusenji nomal "갑작스럽다만 팽―― 에이지 군, 갈까. 미안하네. 여러가지로 번거로워서. 아아…… 자네, 그에게 게스트 패스를"

    voice "audio/voice/v181.mp3"
    f "류센지가 접수처에 말했다"

    voice "audio/voice/v182.mp3"
    f "수상한 젊은이가, 일본 AE사의 실질상 보스를 편하게 불러내었으니, 접수원 하츠네 쪽이 허둥지둥 거동 수상자가 되어 버렸다."

    show hina at Position(xalign = 0.5,yalign = -0.15) with dissolve
    voice "audio/voice/v183.mp3"
    hina2 "네! 지금 바로……"

    voice "audio/voice/v184.mp3"
    ryusenji "D4에 갈 것이니 공동 연구자 패스를 부탁하네"

    voice "audio/voice/v185.mp3"
    hina2 "엣"

    voice "audio/voice/v186.mp3"
    ryusenji "이사회의 결재는 받아 뒀네. 오늘 오전 중에 말야"

    voice "audio/voice/v187.mp3"
    hina2 "네…… 아, 확실히!"

    voice "audio/voice/v188.mp3"
    f "단말을 두드리고 확인하자, 하츠네는 두 번 놀라면서 패스를 발급하는 것이었다."
    
    scene black with blinds
    scene bg_chap_1_2_5 with blinds
    voice "audio/voice/v189.mp3"
    f "발급된 특별한 패스를 들고서 최고 수준으로 경례하고 있는 경비원들을 곁눈질하면서 탐지 게이트를 통과한다."

    voice "audio/voice/v190.mp3"
    f "그것만으로도 에이지는 왠지 굉장히 어른이 된 것 같은 기분이 들었다."

    voice "audio/voice/v191.mp3"
    f "복도를 걷고 있자 지나치는 사원, 연구자들이 류센지에게 인사를 한다."

    voice "audio/voice/v192.mp3"    
    f "에이지는 뒤에 딱 붙어서 두리번거리며 꾸벅꾸벅 마주 인사했다."
    
    voice "audio/voice/v193.mp3"
    f "그건 그것대로, 뭐랄까, 무척 좋은 것이다."
    
    voice "audio/voice/v194.mp3"
    e nomal "류센지 교수님은, 왜 「교수」인 거죠? 사장이라던가 부사장이라던가, 회장 같은 게 아니라"

    voice "audio/voice/v195.mp3"
    ryusenji nomal "대학 교수가 적성에 맞는 거지"

    voice "audio/voice/v196.mp3"
    f "연구자 기질이라는 것이다. AE사의 운영은, 한때의 부하들에게 맡겨두고 있다고 한다."
    
    voice "audio/voice/v197.mp3"
    f "에이지로서도, 대기업의 경영자님에게는 어떻게 접해야 좋을지 모르겠지만, 대학 선생님이라면 다소 이야기하기 쉽다."

    voice "audio/voice/v198.mp3"
    ryusenji "오피스에 가기 전에 들리고 싶은 곳이 있네. 꼭 자네에게 보여주고 싶어서 말야"

    voice "audio/voice/v199.mp3"
    e "뭘까요, 기대되는데!"
    
    voice "audio/voice/v200.mp3"
    ryusenji "이쪽일세"

    voice "audio/voice/v201.mp3"
    f "엘리베이터로 층을 이동하자, 또 경비원이 있는 엄중한 게이트가 있었다"
    
    voice "audio/voice/v202.mp3"
    f "로비에 있었던 공항 같은 탐지 게이트가 아니다. 격벽이다."
    
    voice "audio/voice/v203.mp3"
    f "DDL의 건물 내에서, 이 앞으로부터는 완전히 독립되어 있는 것 같다."
    
    scene bg_chap_1_2_6 with fade

    voice "audio/voice/v204.mp3"
    f "――D4구획"

    voice "audio/voice/v205.mp3"
    ryusenji nomal "여기서부터는 어바딘 일렉트로닉스의 최고 기밀일세. 우리 회사의 미래를 짊어질 핵심이 될 연구가 이루어지고 있지"

    voice "audio/voice/v206.mp3"
    f "류센지가 설명했다."
    
    voice "audio/voice/v207.mp3"
    f "AE사의 최첨단 연구소인 DDL, 그 핵심이 D4구획."
    
    voice "audio/voice/v208.mp3"
    f "에이지는, 스마트폰과 소지품을 경비원에게 맡기게 되었다. 더욱 엄중한 신체검사를 받았다."
    
    voice "audio/voice/v209.mp3"
    e nomal "…………" 

    voice "audio/voice/v210.mp3"
    ryusenji "왜 그러나?"
        
    voice "audio/voice/v211.mp3"
    f "먼저 격벽 게이트를 통과한 류센지가 에이지를 돌아보았다."
    
    voice "audio/voice/v212.mp3"
    e "에- 저기, 마음의 준비가" 
    
    voice "audio/voice/v213.mp3"
    ryusenji "뭘, 약간의 「체험」을 할 뿐이야. 어트랙션은 싫어하는가?"
    
    voice "audio/voice/v214.mp3"
    e "에? 즐거운 거에요?" 
    
    voice "audio/voice/v215.mp3"
    ryusenji "응응…… 유전자 조작으로 공룡을 부활시키거나, 좀비 바이러스 연구를 하고 있는 건 아니지만 말야"
    
    voice "audio/voice/v216.mp3"
    e "그런 전개도 재밌지만요" 
    
    voice "audio/voice/v217.mp3"
    f "류센지의 농담으로 진정하고, 에이지는 D4 게이트를 통과했다"
    
    voice "audio/voice/v218.mp3"
    f "그곳에는――"

    "Chapter 1-2 End..." with Pause(20)
# 챕터 1-3 시작
label Chapter1_3:

    scene black with blinds
    scene bg_chap_1_3 with blinds
   
    voice "audio/voice/v1.mp3"
    "Chapter1-3" "Eiji: Wolf of ninth avenue" 
    
    scene bg_chap_1_2_4 with fade

    show dmap at Position(xalign = 0.5,yalign = 0.3) with dissolve
    voice "audio/voice/v219.mp3"
    f "그곳은 네트워크의 바다."
    
    voice "audio/voice/v220.mp3"
    f "돔형 시어터."

    voice "audio/voice/v221.mp3"
    f "중앙에 선 에이지의 앞에, 와이어 프레임으로 구축된 모형도가 투영된다."

    voice "audio/voice/v222.mp3"
    f "월드 웹―― 파도에 흔들리는 것은 국가, 기업, 연구기관 등의 서버군(群)."
    
    voice "audio/voice/v223.mp3"
    f "그것들은 부유섬, 또는 배 등으로 표현되어 있다."
    
    voice "audio/voice/v224.mp3"
    f "네트워크의 바다로 잠수한다."

    voice "audio/voice/v225.mp3"
    f "그러자 심해 영역에는, 전혀 다른 세계가 펼쳐져 있었다."

    voice "audio/voice/v226.mp3"
    f " ――「디지털 월드」"

    voice "audio/voice/v227.mp3"
    f "돔 시어터에 가이드 음성이 흘러나왔다."
    
    voice "audio/voice/v228.mp3"
    f "와이어 프레임의 모식도가 입체화되어, 선명하게 색이 입혀진다."
    
    voice "audio/voice/v229.mp3"
    "시스템" "그것은, 우리의 현실 세계 리얼 월드와는 다른 세계."
    
    voice "audio/voice/v230.mp3"
    "시스템" "디지털 네트워크 상에 존재하는 전뇌공간이라고 여겨지고 있습니다"
    
    voice "audio/voice/v231.mp3"
    f "네트워크의 바다 너머에 펼치지는 「이세계」디지털 월드."
    
    voice "audio/voice/v232.mp3"
    f "산자수명(山紫水明)――"
    
    voice "audio/voice/v233.mp3"
    f "화질은 거칠었지만, 맑게 갠 아름다운 대자연이었다."
    
    voice "audio/voice/v234.mp3"
    f "현관 로비에서 봤던 환경 영상처럼."
    
    voice "audio/voice/v235.mp3"
    "시스템" "그 디지털 월드에 생식하고 있는 것이, 이――"

    scene bg_chap_1_3_1 with fade

    voice "audio/voice/v236.mp3"
    f "데이터가 입체화되었다."
    
    voice "audio/voice/v237.mp3"
    f "홀로라이즈."
    
    voice "audio/voice/v238.mp3"
    f "전뇌대가 주도하고, AE사가 실용화를 진행시킨 기술이다."
    
    voice "audio/voice/v239.mp3"
    f "거리에서 보이는 3D디지털 사이네즈에도 이 홀로라이즈가 응용되었다."
    
    voice "audio/voice/v240.mp3"
    "시스템" "――이 디지털 몬스터, 「디지몬」입니다!"
    
    voice "audio/voice/v241.mp3"
    f "무언가가 홀로라이즈되었다."
    
    voice "audio/voice/v242.mp3"
    f "언뜻 보기에…… 개구리?"
    
    voice "audio/voice/v243.mp3"
    f "꼬리가 달린 채로 개구리가 갓 된 올챙이다."
    
    voice "audio/voice/v244.mp3"
    f "수박 같은 녹색에 검은 줄무늬. 특징적인 것은 등에 우뚝 솟은 모히칸 컷 같은 등지느러미와, 손발의 갈고리 발톱, 건방지게도 송곳니가 돋아 있다."

    scene bg_chap_1_3_4 with fade
    voice "audio/voice/v245.mp3"
    f "――베타몬 성장기 양서류형 바이러스종"
    
    voice "audio/voice/v246.mp3"
    f "개구리 비슷한 것의 데이터가 표시되었다."

    scene bg_chap_1_2_4 with fade
    show dmap at Position(xalign = 0.5,yalign = 0.3) with dissolve
    voice "audio/voice/v247.mp3"
    "시스템" "디지몬은, 디지털 월드에 살고 있는 정보생명체…… 생명 있는 AI인 것입니다."
   
    voice "audio/voice/v248.mp3"
    f "어떤 교과서에도 실려 있지 않은 것."
    
    voice "audio/voice/v249.mp3"
    e nomal "(생명 있는…… AI……?)"
 
    voice "audio/voice/v250.mp3"
    f "어류, 양서류, 파충류, 포유루, 식물, 곤충, 갑각류, 연체동물, 더 나아가서는 기계나 화학현상"

    voice "audio/voice/v251.mp3"
    f "그 밖의 온갖 다양한, 심지어는 수많은 신불요마(神仏妖魔) 따위의―― 다양한 모티브로 된 디지몬들이, 차례차례로 홀로라이즈해 간다."
    
    voice "audio/voice/v252.mp3"
    f "디지털 월드의 발견과, 그 연구의 역사."
    
    voice "audio/voice/v253.mp3"
    f "디지털 몬스터, 디지몬이란."
    hide dmap with dissolve
    
    show devo at Position(xalign = 0.5,yalign = 0.3) with dissolve
    voice "audio/voice/v254.mp3"
    f "디지몬의 진화(유년기, 성장기, 성숙기, 완전체, 궁극체)."
    
    voice "audio/voice/v255.mp3"
    f "디지몬 분류의 기본이 되는 3개의 속성에 대해.…………"
    
    voice "audio/voice/v256.mp3"
    f "홀로라이즈한 디지몬에 이어서, 그것들이 영상과 함께 설명되어졌다."
    
    voice "audio/voice/v257.mp3"
    e "저 오브제, 로비에 있었던……"
    hide devo with dissolve

    show obj at Position(xalign = 0.5,yalign = 0.3) with dissolve
    voice "audio/voice/v258.mp3"
    f "오브제의 영상에서 3색의 레이저 광선이 뿜어져 나와, 돔 시어터 중앙에 선 에이지를 핥듯이 몇 번이고 반복해서 비추었다."
    
    voice "audio/voice/v259.mp3"
    ryusenji nomal "디지몬 분류학의 기본이 되는 3속성―― 바이러스종, 데이터종, 백신종의 모티브일세"

    voice "audio/voice/v260.mp3"
    f "류센지가 설명했다."
    
    voice "audio/voice/v261.mp3"
    "시스템" "디지몬은, 네트워크상의 신세계인 디지털 월드와의 접촉이, 인류에게 가져다준 과실……!"

    voice "audio/voice/v262.mp3"
    "시스템" "디지몬은 인간 사회에 혁명을 가져다주었습니다."

    voice "audio/voice/v263.mp3"
    "시스템" "디지몬을 AI 툴로서 이용, 응용하는 것으로, 소프트웨어 개발, 암호 시큐리티, AI 신약 개발 같은 분야에서, 눈부신 발견이 있었습니다."

    voice "audio/voice/v264.mp3"
    "시스템" "하지만――"

    voice "audio/voice/v265.mp3"
    f "그것은, 인류의 비밀이다."

    voice "audio/voice/v266.mp3"
    f "전 세계의 사람들 대부분은, 아직까지 디지털 월드의 존재조차 모르는 것이다."
    
    scene bg_chap_1_2_4 with pixellate
    voice "audio/voice/v267.mp3"
    f "갑자기 영상이 흐려졌다."

    voice "audio/voice/v268.mp3"
    f "돔 시어터가 진동한다." with vpunch

    voice "audio/voice/v269.mp3"
    "시스템" " ――설령 알더라도 이해해서는 안 된다."

    voice "audio/voice/v270.mp3"
    f "그 말만 음색이 달랐다. 기계로 가공한 것 같은 목소리다."

    voice "audio/voice/v271.mp3"
    "시스템" "――그것은 겉과 속. 바꾸어 말하면 디지몬은, 사이버 테러의 도구로서 악용할 수도 있습니다."

    voice "audio/voice/v272.mp3"
    "시스템" "소위 말하는 「디지몬 범죄」의 발생입니다"

    voice "audio/voice/v273.mp3"
    f "영상 화면은, 문득 현실세계로 날아갔다."

    scene bg_chap_1_3_2 with flash

    voice "audio/voice/v274.mp3"
    f "그곳은…… 여객기의 객석."

    voice "audio/voice/v275.mp3"
    f "창문 바깥에는, 날개."

    voice "audio/voice/v276.mp3"
    f "제트엔진의 굉음을 울려퍼뜨리며, 비행기가 밤의 구름 위를 날고 있었다."

    voice "audio/voice/v277.mp3"
    f "승객 중 한 사람이 스마트폰으로 기내를 촬영하고 있는…… 그런 영상이다."

    voice "audio/voice/v278.mp3"
    f "한 구석에 담요를 쓰고 자고 있는 것은 촬영좌의 아내인가, 연인인가, 딸인가……."

    voice "audio/voice/v279.mp3"
    "――쿠웅!" with vpunch

    voice "audio/voice/v280.mp3"
    f "리얼한 바람 소리가 에이지의 귀를 막았다."

    voice "audio/voice/v281.mp3"
    f "세계는 노이즈로 가득 차고, 그리고…… 그저, 조용하게."

    voice "audio/voice/v282.mp3"
    f "――――쿠오오오오오오오오오오오" with vpunch

    voice "audio/voice/v283.mp3"
    f "전조도 없이." with vpunch

    voice "audio/voice/v284.mp3"
    f "시야가 기울어진다. 영상의 앵글이 흐려진다. 경보음. 기내에 산소 마스크가 내려온다. 비명, 혼란..." with vpunch
  
    voice "audio/voice/v285.mp3"
    e nomal "(……………………! 에이지는 자기도 모르게 눈을 돌렸다.)"
   
    voice "audio/voice/v286.mp3"
    f "보고 있을 수가 없어졌다. 하지만, 어떻게 할 도리도 없다."

    voice "audio/voice/v287.mp3"
    f "갑자기 기수를 떨어뜨린 여객기는 고도 3만 수천 피트에서, 아래로 똑바로,"

    voice "audio/voice/v288.mp3"
    f "구름을 찢으며 떨어져 갔다."

    scene bg_chap_1_3_1 with flash
    
    voice "audio/voice/v289.mp3"
    f "류센지 토모노리는, 디지털 월드의 발견과 디지털 몬스터의 연구에 있어서 항상 세계를 리드해 왔던 제 1인자다."

    voice "audio/voice/v290.mp3"
    f "애당초 전뇌대의 옆에 이 AE사의 디지털 라보가 있는 것도 그의 존재 때문이다."

    voice "audio/voice/v291.mp3"
    f "한 사람의 연구자가, 이렇게나 대학의 지명도, 기업의 업적에 공헌한 예는 견문이 좁아 알지 못한다."

    voice "audio/voice/v292.mp3"
    f "오늘날의 전뇌대와 AE사의 눈부신 발전은, 류센지 교수의 공헌이 있기에 가능했던 것이다."
    
    voice "audio/voice/v293.mp3"
    ryusenji nomal "훌륭해!"
    
    voice "audio/voice/v294.mp3"
    f "에이지가 납품한 가제트―― 디지몬 독을 검품하고, 류센지는 칭찬과 함께 얼굴에 웃음을 띄었다."

    voice "audio/voice/v295.mp3"
    f "DDL, 류센지의 오피스."

    voice "audio/voice/v296.mp3"
    f "일부에 유리가 쳐진 개별실이다. 기재와 자료, 골판지로 꽉 찬 선반이 엉거주춤하게 늘어선 대학의 연구실 같은 모양새다."

    voice "audio/voice/v297.mp3"
    f "류센지가 디지몬 독을 라보의 기기에 접속시키자, 에이지가 포획한 디지몬이 홀로라이즈되었다."

    voice "audio/voice/v298.mp3"
    f "꼬리가 달린 개구리 비슷한 것."
    
    voice "audio/voice/v299.mp3"
    ryusenji "확실히 의뢰했던 대로 「투베타몬」이다! 보게나, 이 완만하고도 아름다운 곡선을!"
    
    voice "audio/voice/v300.mp3"
    f "류센지는 투베타몬 영상의 윤곽을 사랑스럽다는 듯이 손가락으로 쓰다듬었다."

    voice "audio/voice/v301.mp3"
    f "미지의 디지털 월드에서 발견된 데이터 중에서도, 이 디지털 몬스터・통칭 「디지몬」이라 불리는 AI 프로그램은,"

    voice "audio/voice/v302.mp3"
    f "그 이변성, 확장성, 희소성으로 인해 GriMM의 마켓에서 고가에 취급되고 있었다."

    voice "audio/voice/v303.mp3"
    e nomal "그 녀석 포획하는 데 티라노몬을 3마리나 썼거든요!"

    voice "audio/voice/v304.mp3"
    f "작업용 책상에 짐을 놔 두고, 에이지는 어필했다."

    voice "audio/voice/v305.mp3"
    f "이곳은 D4구획이 아니기에 개인 물품은 돌려받았다."
    
    voice "audio/voice/v306.mp3"
    ryusenji "호오, 그거 큰일이었겠군"

    voice "audio/voice/v307.mp3"
    f "베타몬은, 위기에 처하면 등지느러미 부분을 내던지는 습성이 있다."

    voice "audio/voice/v308.mp3"
    f "투베타몬의 경우에는 등지느러미에서 충격파를 뿜는 것이었다만……"
    voice "audio/voice/v309.mp3"
    f "포획하는 데 사용했던 에이지의 티라노몬(3호)는, 그 기술 「블레이드 핀」에 당해 버렸던 듯하다."
    
    voice "audio/voice/v310.mp3"
    e "네! 그런데 교수님…… 저는 그 투베타몬의 어디가 다른 베타몬이랑 다른지 모르겠는데……"

    voice "audio/voice/v311.mp3"
    ryusenji "뭐라고? 류센지는 약간 표정을 찡그렸다."

    voice "audio/voice/v312.mp3"
    ryusenji "에이지 군, 자네는 모르겠는가? 베타몬과, 이 투베타몬의 차이를!"

    voice "audio/voice/v313.mp3"
    f "클라이언트의 기분을 거스르고 말아, 에이지는 당황했다."
    
    voice "audio/voice/v314.mp3"
    e "에- 그…… 으-응, 색이…… 조금 다른가?"
    
    voice "audio/voice/v315.mp3"
    ryusenji "그렇지! 투베타몬은 살짝 색이 옅다네! 과연, 자네는 차이를 아는 남자로군…… 에이지 군, 이번 보수는 약간 더 신경을 쓰도록 하지"
    
    voice "audio/voice/v316.mp3"
    e "네네네! 감사합니다!"
    
    voice "audio/voice/v317.mp3"
    f "되는대로 말했던 게 정답이었던 듯하다."

    voice "audio/voice/v318.mp3"
    f "이걸로 저녁 식사는 규동에 고기 추가해서 채소절임과 날달걀도 곁들여 먹을 수 있다. 클라이언트도 대만족이다."
    
    scene bg_chap_1_2_4 with fade

    show ryusenji at Position(xalign = 0.5,yalign = - 0.2) with dissolve
    voice "audio/voice/v319.mp3"
    f "류센지는, 투베타몬의 데이터를 라보의 기기에 전송하기 시작했다."
    
    voice "audio/voice/v320.mp3"
    ryusenji "――에이지 군. 그건 그렇고, 아까 그것은 어땠는가?"
    
    voice "audio/voice/v321.mp3"
    e nomal "아까…… D4구획에서 봤던 영상인가요? 엄청 좋았어요!"

    voice "audio/voice/v322.mp3"
    ryusenji "그건, 어떤 프로모션 비디오인데 말이지. 예전에 우리 회사도 엔터테인먼트 부문에 진출할 계획이 있었네. 이름하여 「디지몬 랜드」……"

    voice "audio/voice/v323.mp3"
    e "재밌네요"

    voice "audio/voice/v324.mp3"
    ryusenji "흐음..."

    voice "audio/voice/v325.mp3"
    e "디지털 월드 같은 건 모르는 일반인에게 디지몬을 캐릭터화해서 팔려는 건가!"

    voice "audio/voice/v326.mp3"
    e "디지몬은 생명 있는 AI 생명체…… 생물이라는 설정이 아무튼 좋았었지."

    voice "audio/voice/v327.mp3"
    e "판타지? 픽션? 내가 어린애였으면 푹 빠져들었지도"

    voice "audio/voice/v328.mp3"
    f "에이지는 흘러나오는 대로 감상을 읊었다."

    voice "audio/voice/v329.mp3"
    ryusenji "디지몬은 살아 있다네"

    "Chapter 1-3 End..." with Pause(20)
# 챕터 1-4 시작
label Chapter1_4:

    scene black with blinds
    scene bg_chap_1_4 with blinds
   
    voice "audio/voice/v1.mp3"
    "Chapter1-4" "Eiji: Wolf of ninth avenue" 

    scene bg_chap_1_2_4 with fade

    show ryusenji at Position(xalign = 0.5,yalign = - 0.2) with dissolve
    voice "audio/voice/v330.mp3"
    f "류센지가 말했다. 「디지몬은 살아있다」고."

    voice "audio/voice/v331.mp3"
    e nomal "――정말로 디지몬이 살아있다면 즐겁겠네요!"

    voice "audio/voice/v332.mp3"
    e "지금도 디지몬을 디지털 펫처럼 기르는 취미의 매니아도 있고, 류센지 교수님 같은 콜렉터도 있지만."

    voice "audio/voice/v333.mp3"
    e "나 같은 크래커에게 있어서 디지몬은…… 편리한 AI 툴이려나."
    
    voice "audio/voice/v334.mp3"
    f "에이지에게 있어서 디지몬은 소중한, 일 도구다."

    voice "audio/voice/v335.mp3"
    f "에이지는, 지금은 티라노몬을 애용하고 있다"
 
    voice "audio/voice/v336.mp3"
    f "디지털 월드에서는 비교적 자주 포획되는 디지몬으로, GriMM에서 많은 개체가 거래되고 있었다."

    voice "audio/voice/v337.mp3"
    e "흠... 언제, 어디에 생기는 거에요? 그 「디지몬 랜드」."

    voice "audio/voice/v338.mp3"
    ryusenji "영원히 서랍 속에 묻혀버렸다는 경우일세."
    
    voice "audio/voice/v339.mp3"
    f "류센지는 안타깝다는 듯이 한숨을 쉬었다."

    voice "audio/voice/v340.mp3"
    e "어라."

    voice "audio/voice/v341.mp3"
    ryusenji "현실적으로 어려워. 그래서 디지털 월드는 「인류의 비밀」인 채야"
    
    scene bg_chap_1_3_3 with fade
    voice "audio/voice/v342.mp3"
    f "류센지의 말에, 에이지의 뇌리에 아까 봤던 항공기 낙하 영상이 스쳐갔다."

    scene bg_chap_1_2_4 with fade
    show ryusenji at Position(xalign = 0.5,yalign = -0.2) with dissolve
    voice "audio/voice/v343.mp3"
    e nomal"디지몬을 범죄에 사용하는 녀석들이 있으니까 말이죠. 동업자…… 질 나쁜 크래커지만"

    voice "audio/voice/v344.mp3"
    f "크래커는 대부분 그레이 존의 존재지만, 그 중에서도 흑백이 갈린다."

    voice "audio/voice/v345.mp3"
    f "흰색에 가까운 그레이와, 새까만 검정에 가까운 그레이."

    voice "audio/voice/v346.mp3"
    f "이야기 해 보면 좋은 녀석과 진짜로 위험한 녀석, 범죄자, 전 인류의 적 레벨인 녀석까지."

    voice "audio/voice/v347.mp3"
    f "어쨌든――"

    voice "audio/voice/v348.mp3"
    f "작금에 이곳저곳에서 빈발하고 있는 네트워크 장해, 부정 접속에 의한 정보 절도, 사이버 테러"

    voice "audio/voice/v349.mp3"
    f "거기에 사실은 적지 않은 AI 툴로서 디지몬이 관계되어 있다."

    voice "audio/voice/v350.mp3"
    f "그 영상처럼, 테러리스트가 사용한 디지몬이 실제로 비행기를 떨어뜨렸다는 걸로 받아들여진 사건도 있었다."

    voice "audio/voice/v351.mp3"
    f "그 사실은, 물론 공공연하게 퍼져 있지 않다."

    voice "audio/voice/v352.mp3"
    f "디지몬과 디지털 월드에 관한 것은 일반적으로는 알려져 있지 않았다."

    voice "audio/voice/v353.mp3"
    f "전 세계의 수뇌들과 국제 기관이, 그 존재 자체를 은폐―― 숨겨왔기 때문이다."

    voice "audio/voice/v354.mp3"
    f "어쨌든 간에, 만약 테마파크의 캐릭터가 범죄자의 도구로서 사이버 테러를 일으켰다……"

    voice "audio/voice/v355.mp3"
    f "같은 일이 일어났다간 불상사에도 정도가 있다."
    
    voice "audio/voice/v356.mp3"
    ryusenji"디지털 월드와 디지몬에 관한 것은 세간에 널리 알린다는 것은 디지몬 범죄에 대해 세계에 공표한다는 것과 이어지네. 어떻게 될 거라고 생각하나?"

    voice "audio/voice/v357.mp3"
    e "패닉!"

    voice "audio/voice/v358.mp3"
    ryusenji "그 말 그대로다."

    voice "audio/voice/v359.mp3"
    f "디지몬은 이세계에서 온 침략자, 라던가, 불안을 조장하는 게 일인 매스컴이 떠들어 댈 것이리라."
    
    voice "audio/voice/v360.mp3"
    f "알기 쉽게 단락적으로, 디지털 월드와 디지몬은 악, 이라고 규정될지도 모른다."
    
    voice "audio/voice/v361.mp3"
    ryusenji "아직도 인류의 과반수는 디지털 월드를 모르네."

    voice "audio/voice/v362.mp3"
    ryusenji "알고는 있더라도 이해는 하고 있지 못 해"
    
    voice "audio/voice/v363.mp3"
    f "류센지는 천재답게 에이지에게는 어려운 말을 입에 담았다."

    voice "audio/voice/v364.mp3"
    ryusenji "설마 네트워크 저편에 현실세계와는 다른 이세계가 있다는……"

    voice "audio/voice/v365.mp3"
    ryusenji "디지몬이라는 생명이 살고 있었다는 것은."

    voice "audio/voice/v366.mp3"
    f "알고는 있어도 이해는 하지 못하고 있다."

    voice "audio/voice/v367.mp3"
    e "류센지 교수님..."

    voice "audio/voice/v368.mp3"
    f "그것이 크래커―― 디지털 월드에서, 디지몬을 사용해 일을 하는 자신에게 향한 말이기도 하다는 것을, 에이지는 느꼈다."

    voice "audio/voice/v369.mp3"
    f "디지몬은 살아있다."

    voice "audio/voice/v370.mp3"
    ryusenji "크래커 팽…… 에이지 군, 알고 싶지는 않은가?"

    voice "audio/voice/v371.mp3"
    ryusenji "리얼 월드와 디지털 월드, 두 세계의 진실을."

    voice "audio/voice/v372.mp3"
    ryusenji "세계의 뒤편을 보고 싶지는 않은가?"

    voice "audio/voice/v373.mp3"
    e "그야…… 보고 싶죠!"

    voice "audio/voice/v374.mp3"
    f "에이지는 흥분했다."

    voice "audio/voice/v375.mp3"
    e "――그야 전 모르니까요! 제게 있어서 디지털 월드는…… 그 디지몬 독의 흑백 화면의 정보, 그게 전부니까요."

    voice "audio/voice/v376.mp3"
    e "하지만 교수님, 당신이 보고 있는…… 봐 왔던 세상은 분명, 다르죠?"

    voice "audio/voice/v377.mp3"
    e "그렇지, 아까 영상에서 봤던 경치――"

    voice "audio/voice/v378.mp3"
    f "―네트워크의 바다와 리얼월드, 그리고 디지털 월드."

    voice "audio/voice/v379.mp3"
    f "노이즈 너머로 엿보였던, 그 세계는……."

    voice "audio/voice/v380.mp3"
    ryusenji "자네에게 보여준 영상이, 어째서 「D4」…… 우리 회사의 최고 기밀인지."

    voice "audio/voice/v381.mp3"
    ryusenji "인류의 비밀이 되어 있는지, 알겠는가?"

    voice "audio/voice/v382.mp3"
    e "그건."

    voice "audio/voice/v383.mp3"
    f "에이지는 번뜩였다."
    
    voice "audio/voice/v384.mp3"
    e "그 영상이 진짜여서인가?!" with vpunch

    voice "audio/voice/v385.mp3"
    f "픽션인 프로모션 비디오가 아니라, 디지털 월드를 관측한 영상이었으니까……"
    
    voice "audio/voice/v386.mp3"
    ryusenji "그래…… 그 경치는, 관측 데이터에 기반하여 AI가 생성한 진짜 디지털 월드의 상상화다."

    voice "audio/voice/v387.mp3"
    ryusenji "그리고 디지몬은 디지털 월드에서 정말로 살고 있지."

    voice "audio/voice/v388.mp3"
    ryusenji "지구 외 생명체는 외우주가 아니라 디지털 네트워크상에 있었다는 걸세."
    
    voice "audio/voice/v389.mp3"
    f "류센지는, 똑바로 에이지를 봤다."

    voice "audio/voice/v390.mp3"
    f "그가 하고 있는 말은, 예시를 든 것이나, 사물을 인식하는 관점을 설명하는 이야기가 아니었다."
    
    voice "audio/voice/v391.mp3"
    e "디지몬은 살아 있다……!"

    scene bg_chap_1_3_1 with fade
    voice "audio/voice/v392.mp3"
    f "에이지는 홀로라이즈한 투베타몬을 봤다."

    voice "audio/voice/v393.mp3"
    f "살아 있다."

    voice "audio/voice/v394.mp3"
    f "그렇다면, 지금까지 AI 툴로서 다뤄왔던 티라노몬들도……? 다른, 모든 디지몬들도?"

    voice "audio/voice/v395.mp3"
    ryusenji nomal "디지털 월드의 존재방식, 디지몬의 존재방식을, 이 눈으로, 직접 보는 것."

    voice "audio/voice/v396.mp3"
    ryusenji "가상 모니터와 관측 데이터가 아닌, 인간의 오감으로 직접 디지털 월드를, 파악하는 것."

    voice "audio/voice/v397.mp3"
    ryusenji "리얼월드와 디지털 월드의 「굴레」를 뛰어넘는다."

    voice "audio/voice/v398.mp3"
    ryusenji "있는 그대로. 그것이야말로 내가…… 이 류센지 토모노리가 인생을 걸고 몰두한 연구다."

    voice "audio/voice/v399.mp3"
    ryusenji "그렇기에 나의 모든 것이 「D4」인 것이지"

    voice "audio/voice/v400.mp3"
    f "투베타몬의 데이터 이동이 완료됐다."
    
    voice "audio/voice/v401.mp3"
    f "류센지는 에이지의 납품용 디지몬 독을 기기에서 분리하고, 손가락으로 집고서 바라보았다."
    
    voice "audio/voice/v402.mp3"
    e nomal "………… 아, 감사합니다"

    voice "audio/voice/v403.mp3"
    f "에이지는 손을 내밀었다."

    voice "audio/voice/v404.mp3"
    f "류센지는 디지몬 독을 내팽개쳐버렸다."

    voice "audio/voice/v405.mp3"
    e "에에에에에??"
    
    voice "audio/voice/v406.mp3"
    f "깜짝 놀랄 틈도 없이 에이지는 헤드 슬라이딩을 할 기세로 디지몬 독이 쓰레기통에 떨어지기 직전에 캐치했다."
    
    voice "audio/voice/v407.mp3"
    e "뭐 하시는 거에요, 교수님!"  with vpunch
    
    voice "audio/voice/v408.mp3"
    f "기세가 지나쳐서 쓰레기통에 얼굴부터 다이브해버렸다."

    voice "audio/voice/v409.mp3"
    f "에이지는 독은 파츠를 짜맞춘 자작품이다."
    
    voice "audio/voice/v410.mp3"
    f "정크(쓰레기)라고는 해도 돈이 들어갔다."

    voice "audio/voice/v411.mp3"
    ryusenji "그거, 메모리 영역에 에러가 있었네"
    
    voice "audio/voice/v412.mp3"
    e "진짜임까?!" with vpunch

    voice "audio/voice/v413.mp3"
    f "류센지는 디지몬 콜렉터다."
    
    voice "audio/voice/v414.mp3"
    f "데이터의 컨디션에는 남들의 배는 신경을 쓰는 것이다."
    
    voice "audio/voice/v415.mp3"
    ryusenji "구식은 사용하지 않는 편이 좋네. 내가 맡긴 일을 할 때는, 특히 더……"

    voice "audio/voice/v416.mp3"
    ryusenji "하마터면 투베타몬의 데이터가 망가질 뻔했어"
    
    voice "audio/voice/v417.mp3"
    e "그렇다고 버릴 건 없잖아요……"

    voice "audio/voice/v418.mp3"
    e "저기 말이죠 교수님, 프리 크래커의 지갑 사정은 대기업하고는 다르다구요?"

    voice "audio/voice/v419.mp3"
    e "이것도 저것도 자가 지출, 영수증 같은 것도 못 끊고,"

    voice "audio/voice/v420.mp3"
    e "여기 있는 것처럼 하이스펙 기기를 맘대로 착취할 수 있는 게 아니라고요."
    
    voice "audio/voice/v421.mp3"
    ryusenji "흠."

    voice "audio/voice/v422.mp3"
    e "...... 네?"

    voice "audio/voice/v423.mp3"
    f "에이지는 어리둥절했다."

    voice "audio/voice/v424.mp3"
    f "류센지는, 조금 독특한 간격을 두고 이야기를 한다."

    voice "audio/voice/v425.mp3"
    f "뭐라 해도 일본이 자랑하는 천재 과학자다."

    voice "audio/voice/v426.mp3"
    f "어딘가 남들과 다른 부분이 있는 것 정도는 용서받을 수 있는 것일까."

    voice "audio/voice/v427.mp3"
    ryusenji "그거 미안하군. 아아…… 그럼 마침 잘 됐어. 팔을 내보게"
    
    voice "audio/voice/v428.mp3"
    e "?"

    voice "audio/voice/v429.mp3"
    f "뭐가 마침 잘 된 것인지는 모르겠지만, 시키는 대로 한다."

    voice "audio/voice/v430.mp3"
    f "류센지는 에이지의 왼손목에 무언가를 채웠다."

    voice "audio/voice/v431.mp3"
    f "에이지는…… 숨을 삼켰다."

    scene bg_chap_1_4_1 with fade

    voice "audio/voice/v432.mp3"
    e nomal "............ 읏!"

    voice "audio/voice/v433.mp3"
    f "이런 기분이 든 것은 언제 이후인가……."
    
    voice "audio/voice/v434.mp3"
    f "어렸을 무렵, 새로운 게임기를 부모님이 사 주셨을 때? "
    
    voice "audio/voice/v435.mp3"
    f "처음으로 스마트폰을 사 주셨을 때?"
    
    voice "audio/voice/v436.mp3"
    f "아니, 그 몇 배나……!"
    
    voice "audio/voice/v437.mp3"
    f "이 몸에 찬 것만으로도 세계가 넓어져 가는 예감은."
    
    voice "audio/voice/v438.mp3"
    ryusenji nomal "이걸, 자네에게 주지."
    
    voice "audio/voice/v439.mp3"
    f "손목시계형 가제트였다."
    
    voice "audio/voice/v440.mp3"
    e "어바딘 일렉트로닉스제…… 최신형 디지몬 독?"
    voice "audio/voice/v441.mp3"
    e "게다가 스마트 워치 타입!"

    voice "audio/voice/v442.mp3"
    f "에이지는 점프해서 3회전 반 한 것 같은 기분이었다."

    voice "audio/voice/v443.mp3"
    f "원래부터 AE사의 제품은 디지몬 독으로 개조하기 쉬워 크래커 사이에서는 평가가 높다."

    voice "audio/voice/v444.mp3"
    f "게다가, 이것은 순정품. 디지몬에 얽힌 것이라 기업 비밀에 속해 있는 물건이다."

    voice "audio/voice/v445.mp3"
    f "――디지몬 링커"

    voice "audio/voice/v446.mp3"
    ryusenji "내가 설계에 관련되어 있는 제품의 시작품일세"

    voice "audio/voice/v447.mp3"
    e "류센지 교수님…… 당신, 알면 알수록 굉장해요!" with vpunch

    voice "audio/voice/v448.mp3"
    f "에이지의 팔에서 손목시계형 디지몬 독이 자동 셋업을 시작한다."

    voice "audio/voice/v449.mp3"
    ryusenji "나는 디지몬 독 부문의 기술 통괄 책임자이기도 하거든."

    voice "audio/voice/v450.mp3"
    ryusenji "그것에는 생체 정보…… 바이탈 센서가 달려있어서 지금 등록한 자네밖에 쓸 수 없어"

    voice "audio/voice/v451.mp3"
    e "오오! 내 전용!"
    
    voice "audio/voice/v452.mp3"
    ryusenji "의료기기 클래스의 센서니까. 맥박, 혈압, 호흡, 체온, 그런 걸 전부 기록하고 있으니."

    voice "audio/voice/v453.mp3"
    ryusenji "우리의 라이프 서포트로 24시간, 안심할 수 있는 의료 서포트 체제도 포함이다"

    voice "audio/voice/v454.mp3"
    e "건강해져 버리겠는걸"
    
    voice "audio/voice/v455.mp3"
    f "에이지는 기세를 타서 대답했다"
    
    voice "audio/voice/v456.mp3"
    ryusenji "홀로라이즈 기능도 서포트하고 있네." 

    voice "audio/voice/v457.mp3"
    ryusenji "원래 디지몬의 홀로라이즈는 이 DDL 외에, 한정된 시설 내에서만 허가되어 있지만…… 특례다"
    
    voice "audio/voice/v458.mp3"
    f "어쨌든 간에 특별, 특별, 특별취급."
    
    voice "audio/voice/v459.mp3"
    e "하지만 시작품이라니…… 괜찮은 거에요? 뭔가 뒷사정이 있는 건"

    voice "audio/voice/v460.mp3"
    ryusenji "안심하게나. 이건 나 개인이, 자네에게 주는 선물이야"
    
    voice "audio/voice/v461.mp3"
    e "진심 쩔어!" with vpunch
    
    voice "audio/voice/v462.mp3"
    ryusenji "그럼, 그래서 말인데."
    
    voice "audio/voice/v463.mp3"
    e "거봐요, 역시 뒷사정 있네요! 교수님의 성격을 점점 알 것 같은데요, 저"
     
    voice "audio/voice/v464.mp3"
    f "농담으로 분위기를 흐리긴 했지만 에이지는 이 스마트 워치형 디지몬 독을 포기할 생각은 없다."
    
    voice "audio/voice/v465.mp3"
    f "갖고 싶다."
    
    voice "audio/voice/v466.mp3"
    f "디지몬 링커는 과장 없이 에이지의 자작 독하고는 격이 다른"
    
    voice "audio/voice/v467.mp3"
    f "압도적인 다른 성능이 있을 터이다."

    voice "audio/voice/v468.mp3"
    ryusenji "그래서 크래커 팽을 눈여겨보고, 다음 일을 부탁하고 싶네."
    
    voice "audio/voice/v469.mp3"
    e "하겠습니다."
    
    voice "audio/voice/v470.mp3"
    ryusenji "즉답인가. 실로 좋군, 자네의 그런 점이 좋네"
    
    voice "audio/voice/v471.mp3"
    f "류센지는 에이지의 팔을 잡고, 디지몬 링커 측면에 있는 스위치를 눌렀다."
    
    voice "audio/voice/v472.mp3"
    f "화면이 어렴풋이 반짝였다."
    
    scene bg_chap_1_4_2 with fade
    voice "audio/voice/v473.mp3"
    f "신기한 불꽃이, 시계 화면에서 흔들린 것처럼 보였다."


    scene bg_chap_1_4_3 with fade
    voice "audio/voice/v474.mp3"
    f "――루가몬 성장기 마수형 바이러스종"

    scene bg_chap_1_4_2 with fade
    voice "audio/voice/v475.mp3"
    f "작은 컬러 화면에는 본 적 없는 디지몬이 비춰져 있었다."
    
    voice "audio/voice/v476.mp3"
    f "에이지는 눈을 가늘게 떴다."
    
    voice "audio/voice/v477.mp3"
    e nomal "강아지…… 개?" 

    scene black with blinds
    scene bg_chap_1_2_2 with blinds
    voice "audio/voice/v478.mp3"
    f "류센지 교수에게서 새로운 의뢰를 받은 에이지는 혼자서 게이트를 빠져나와 1층의 접수 홀로 돌아왔다."
    
    voice "audio/voice/v479.mp3"
    e nomal "리얼월드와 디지털 월드의 굴레를 뛰어넘는다…… 인가." 
    
    voice "audio/voice/v480.mp3"
    f "홀 중앙에는 그 미츠도모에 오브제가 홀로라이즈 되어 있다."

    show hina at Position(xalign = 0.5,yalign = -0.15) with dissolve
    voice "audio/voice/v481.mp3"
    hina2 "아, 수고하셨습니다!"
    
    voice "audio/voice/v482.mp3"
    f "접수처에서, 하츠네 쪽에서 말을 걸어 왔다."

    voice "audio/voice/v483.mp3"
    e "패스는 여기에 내면 될까?"

    voice "audio/voice/v484.mp3"
    hina2 "여기에 반납해주세요. 감사합니다."

    voice "audio/voice/v485.mp3"
    f "에이지는 패스를 건넸다."

    voice "audio/voice/v486.mp3"
    f "그 팔에 채워진 것을, 하츠네가 눈치챘다."
    
    voice "audio/voice/v487.mp3"
    hina2 "......응?"

    voice "audio/voice/v488.mp3"
    e "아, 이거? 류센지 교수님한테서 받았어. ……알고 있어? 디지몬 독"

    voice "audio/voice/v489.mp3"
    f "에이지는 신품 스마트 워치형 가제트를 하츠네에게 내보였다."
    
    voice "audio/voice/v490.mp3"
    f "하츠네는 두리번두리번 주변을 둘러보고 속삭이며 대답했다."
    
    voice "audio/voice/v491.mp3"
    hina2 "기밀이죠, 최신형?" 
    
    voice "audio/voice/v492.mp3"
    f "접수원라는 입장이어서인지, 그럭저럭 정보통인 듯하다."
    
    voice "audio/voice/v493.mp3"
    e "시작품 테스트긴 하지만 말이지-"
    
    voice "audio/voice/v494.mp3"
    hina2 "굉장해요. 그 류센지 교수님에게서 직접 테스트 의뢰를 받다니…… "
    
    voice "audio/voice/v495.mp3"
    hina2 "나가스미 씨, 무척이나 신뢰받고 있으시네요"
    
    voice "audio/voice/v496.mp3"
    f "아부하는 게 아니라, 하츠네는 진심으로 놀라고 있었다."
    
    voice "audio/voice/v497.mp3"
    e "응-…… 그런가. 반대로 묻겠는데, 그런 거야?"
    
    voice "audio/voice/v498.mp3"
    hina2 "절대로 그래요……! 류센지 교수님은 그래 보여도 무척――"
    
    voice "audio/voice/v499.mp3"
    hina2 "하츠네는 더욱 목소리를 줄였다."
    
    voice "audio/voice/v500.mp3"
    hina2 "까다로우신 부분이 있으니까"
    
    voice "audio/voice/v501.mp3"
    e "아-, 독특하지."
    
    voice "audio/voice/v502.mp3"
    f "에이지는 자기도 모르게 내뱉어 버렸다."
    
    voice "audio/voice/v503.mp3"
    f "하츠네의 태도가 처음과는 전혀 달랐기 때문이었다."
    
    voice "audio/voice/v504.mp3"
    f "하지만, 이건 이것대로 나쁘지 않다."

    voice "audio/voice/v505.mp3"
    e "그럼, 또 봐."
    
    voice "audio/voice/v506.mp3"
    hina2 "아, 나가스미 씨."
    
    voice "audio/voice/v507.mp3"
    e "에이지면 돼."
    
    voice "audio/voice/v508.mp3"
    hina2 "저도…… 하츠네쨩도 하츠넷치여도 괜찮아요! "
    
    voice "audio/voice/v509.mp3"
    hina2 "그래서…… 에이지 씨의 입장 기록 말인데요."
    
    voice "audio/voice/v510.mp3"
    hina2 "직업란 쪽이 아직 공란이어서! 괜찮으시다면 가르쳐 주실 수 있으신가요……?"
    
    voice "audio/voice/v511.mp3"
    f "하츠네는 무언가를 멋대로 기대하고 안절부절하고 있었다."
    
    voice "audio/voice/v512.mp3"
    e "직업?"
    
    voice "audio/voice/v513.mp3"
    f "에이지는 잠시 생각에 잠겼다"
    
    voice "audio/voice/v514.mp3"
    f "프리터…… 는 직업이 아니다. 정식 직업이 없을 뿐이다."
    
    voice "audio/voice/v515.mp3"
    e "――나가스미 에이지, 직업은 크래커"
    
    voice "audio/voice/v516.mp3"
    hina2 "에-"
    
    voice "audio/voice/v517.mp3"
    f "하츠네는 오늘 중에서 가장 미묘한 반응을 돌려주는 것이었다."

    "Chapter 1-4 End..." with Pause(20)
# 챕터 1-5 시작
label Chapter1_5:

    scene black with blinds
    scene bg_chap_1_5 with blinds

    voice "audio/voice/v1.mp3"
    "Chapter1-5" "Eiji: Wolf of ninth avenue" 
    
    voice "audio/voice/v1_5_1.mp3"
    f "디지털 월드에서 디지몬을 입수하는 방법은, 크게 두 가지."
    
    voice "audio/voice/v1_5_2.mp3"
    f "한 가지는, 툴을 구사하여 디지몬을 포획하는 것."
    
    show digitama at Position (xalign = 0.5, yalign = 0.35) with dissolve
    voice "audio/voice/v1_5_3.mp3"
    f "또 한 가지는 디지몬의 알――"
    
    voice "audio/voice/v1_5_4.mp3"
    f "디지타마를 채취하는 것이다."

    voice "audio/voice/v1_5_5.mp3"
    f "알이라고는 해도 새나 물고기의 알과는 조금 다르다."
    voice "audio/voice/v1_5_6.mp3"
    f "우선, 현재의 정설로는 디지몬에게는 성별이 없다." 
    voice "audio/voice/v1_5_7.mp3"
    f "암수가 없다."
    voice "audio/voice/v1_5_8.mp3"
    f "그럼, 어떻게 디지몬이 탄생하는가 하면, 이것도 정설로는 디지타마에서 태어난다"
    voice "audio/voice/v1_5_9.mp3"
    f "디지몬은 죽으면 그 영혼이라고 할 법한 데이터를 남긴다."
    voice "audio/voice/v1_5_10.mp3"
    f "그렇게 하여 디지털 월드의 어딘가에, 또, 새로운 디지타마로서 부활한다고 한다."
    voice "audio/voice/v1_5_11.mp3"
    f "마치 윤회전생을 떠올리게 하나, 디지몬의 생태는 모르는 것투성이다."
    voice "audio/voice/v1_5_12.mp3"
    f "인류는 아직도 디지털 월드의 아주 일부밖에 몰랐다."
    
    scene black with blinds
    scene bg_chap_1_5_1 with blinds
    voice "audio/voice/v1_5_13.mp3"
    f "밝지 않는 밤은 있다."

    voice "audio/voice/v1_5_14.mp3"
    f "어디까지나, 언제까지나 계속되는 박모(薄暮. 저녁노을), 황혼의 하늘. "
    voice "audio/voice/v1_5_15.mp3"
    f "아니 하늘처럼 보이는 것은 네트워크의 바다"
    voice "audio/voice/v1_5_16.mp3"
    f "구름처럼 보이는 것은 웹의 파도"
    voice "audio/voice/v1_5_17.mp3"
    f "별똥별은 정보의 스트림……"
    voice "audio/voice/v1_5_18.mp3"
    f "이곳은 하늘에 있는 물 밑바닥."
    voice "audio/voice/v1_5_19.mp3"
    f "일렁이는 옅은 빛은, 아득한 해면 위에 있는 리얼월드에서 오고 있다."
    voice "audio/voice/v1_5_20.mp3"
    f "네트워크의 세계는 맑고도 아름답게."
    voice "audio/voice/v1_5_21.mp3"
    f "하지만 누군가가 살고 있는 세계에는 예외 없이, 어딘가 망가져서 정체되어 있었다."
    voice "audio/voice/v1_5_22.mp3"
    f "녹슨 철 비가 퍼붓고, 바람은 피 냄새가 난다."
    voice "audio/voice/v1_5_23.mp3"
    f "화학물질의 자극적인 냄새가 감도는 오수가 거품을 일으키며 밀려오고 있다."
    voice "audio/voice/v1_5_24.mp3"
    f "시궁창…… 이라고 할 수준이 아니었다."
    voice "audio/voice/v1_5_25.mp3"
    f "광독(鉱毒)이 흐르는 봉쇄도시도 이렇게나―― "
    voice "audio/voice/v1_5_26.mp3"
    f "군데군데 기묘한 형광색으로 반짝이고, 정체를 알 수 없는 쓰레기 데이터가 한데 모인 흐름이"
    voice "audio/voice/v1_5_27.mp3"
    f "강둑을 깎아내면서 울타리가 부러진 강 입구에서 밖으로 토해내져 간다."
    voice "audio/voice/v1_5_28.mp3"
    f "디지털 월드에「흐름」이 있는 것은 어째서일까."
    voice "audio/voice/v1_5_29.mp3"
    f "시간의 흐름. 물질의 흐름, 날씨 등의 자연현상이 있는 것은."

    scene bg_chap_1_5_2 with fade
    voice "audio/voice/v1_5_30.mp3"
    f "명백하게 사회생활이 만들어낸, 이런 쓰레기의 산이 있는 것은."
    voice "audio/voice/v1_5_31.mp3"
    f "일설에서는 인간사회를 비롯한 리얼월드와의 네트워크를 경유한 접촉이 디지털 월드에, 이만큼의 데이터 다양성과 순환을 가져왔다고 한다."
    voice "audio/voice/v1_5_32.mp3"
    f "만약, 그게 사실이라면."
    voice "audio/voice/v1_5_33.mp3"
    f "한때 신대륙을 발견한 유럽인이, 현지의 제국을 멸망시킬 정도의 병원균을 가져왔듯이."
    voice "audio/voice/v1_5_34.mp3"
    f "성간 운행이 가능해진 SF세계에서, 우주선에 붙어있던 미지의 세균이 무시무시한 크라이시스를 일으키는 패닉 무비의 줄거리처럼."
    voice "audio/voice/v1_5_35.mp3"
    f "인류와 디지털 월드의 접촉은 이 이세계와 그곳에서 사는 생물을, 그때까지, 그 후로도 일변시켜버렸다는 말이 된다."
    voice "audio/voice/v1_5_36.mp3"
    f "좋은 일인가, 나쁜 일인가. 그것은 알 수 없다."
    voice "audio/voice/v1_5_37.mp3"
    f "선악에「굴레」를 채우는 것은 경찰이 할 일이 아니니까."
    voice "audio/voice/v1_5_38.mp3"
    f "에리어에는, 보이지만 않을 뿐, 몇 개의 의도가 꿈틀거리고 있었다."
    voice "audio/voice/v1_5_39.mp3"
    f "헤드업 가상 모니터에 와이어 프레임 모식도가 떠오른다."

    scene bg_chap_1_5_3 with fade
    voice "audio/voice/v1_5_40.mp3"
    f "――「철창해안(鉄錆海岸. 라스트 코스트)」"
    voice "audio/voice/v1_5_41.mp3"
    f "누가 부른 것인지, 그런 이름이 붙여진 붉은 사철의 해안이다."
    voice "audio/voice/v1_5_42.mp3"
    f "이곳에는 쓰레기 데이터의 흐름에 모인 디지타마가 자주 표착한다."
    voice "audio/voice/v1_5_43.mp3"
    f "그것을 노린 밀어꾼도."
    voice "audio/voice/v1_5_44.mp3"
    "디지대 대원" "「부반장님! 수상한 디지몬 반응 확인」"
    voice "audio/voice/v1_5_45.mp3"
    f "경찰 무선 보이스 채팅이 들어온다."
    voice "audio/voice/v1_5_46.mp3"
    f "가상 모니터의 강 입구 에리어 맵에 빨간 점이 흩어져 있었다. 미확인 디지몬이다."
    voice "audio/voice/v1_5_47.mp3"
    hime nomal "여기는 타마히메, 계속 색적할 것"

    scene bg_chap_1_5_4 with fade
    voice "audio/voice/v1_5_48.mp3"
    f "강 표면에서 잠망경처럼 튀어나온 그녀의 디지몬의 「눈」을 빌린다."

    scene bg_chap_1_5_5 with fade
    voice "audio/voice/v1_5_49.mp3"
    "디지대 대원" "상세 색적합니다…… 에스피몬, 성장기, 사이보그형, 바이러스종"

    scene bg_chap_1_5_4 with fade
    voice "audio/voice/v1_5_50.mp3"
    hime nomal "확인했다. 양철 장난감인가"
    voice "audio/voice/v1_5_51.mp3"
    f "뭐라고도 설명하기 힘든, 보고서로 작성하기 힘든 모습을 한 디지몬이다."
    voice "audio/voice/v1_5_52.mp3"
    f "척 봤을 때는 레트로한 쇼와 코미디 계열 로봇 방송에 나오는 장난감……?"
    voice "audio/voice/v1_5_53.mp3"
    f "뒤집어 놓은 눈사람 같은 가분수 몸통에, 매니퓰레이터로 된 팔 부분, 다리 부분에는 로켓 분사구의 노즐뿐이다."
    voice "audio/voice/v1_5_54.mp3"
    "디지대 대원" "총 4체입니다!"
    voice "audio/voice/v1_5_55.mp3"
    hime "크래커가 안 붙어 있군……! ４체 모두 Bot냐 이 자식들"
    voice "audio/voice/v1_5_56.mp3"
    f "쯧 하고 혀를 찼다."
    voice "audio/voice/v1_5_56_1.mp3"
    f "Bot(봇)이란 경찰 속어로, 툴로 인한 자동 조종 상태의 디지몬을 가리킨다."
    voice "audio/voice/v1_5_57.mp3"
    "디지대 대원" "요즘 들어 크래커 사이에서 유행하는 디지몬입니다"
    voice "audio/voice/v1_5_58.mp3"
    hime "사이보그형은 툴과 상성이 좋으니까 말야. 초심자 체포 들어가신다"
    voice "audio/voice/v1_5_59.mp3"
    f "디지털 월드에 디지몬을 풀어놓고 방치"
    voice "audio/voice/v1_5_60.mp3"
    f "AI 툴에 맡겨놓고 일정 범위를 탐색해서, 노리던 데이터를 포획 채취한다. "
    voice "audio/voice/v1_5_61.mp3"
    f "자주 있는 크래커의 수법이다."
    voice "audio/voice/v1_5_62.mp3"
    f "이것이 리얼에서의 서버라면 노리는 것은 기업 비밀이나 개인정보 등이 되겠지만……"
    voice "audio/voice/v1_5_63.mp3"
    f "이런 디지털 월드의 해안에서 크래커의 벌이가 될 법한 것이라고 한다면"
    voice "audio/voice/v1_5_64.mp3"
    "크래커1" "――디지타마, 몇 개나 주웠어?" with blinds
    voice "audio/voice/v1_5_65.mp3"
    "크래커2" "――아직, 한 개." with blinds
    voice "audio/voice/v1_5_66.mp3"
    f "도청."
    voice "audio/voice/v1_5_67.mp3"
    f "크래커 무리의 GriMM에서의 보이스 채팅 회화를 주워올린다."
    voice "audio/voice/v1_5_68.mp3"
    f "목소리가 어리다. 보이스 체인저를 사용한 흔적 없음."
    voice "audio/voice/v1_5_69.mp3"
    hime "보이스채팅 다 흘리고, 전부 바로 누설…… 초보자냐?"
    voice "audio/voice/v1_5_70.mp3"
    f "디지몬은 bot이지만 조작하는 크래커들도 온라인으로 이어져 있었다."
    voice "audio/voice/v1_5_71.mp3"
    f "말하자면 넷 게임 감각인 것이다."
    voice "audio/voice/v1_5_72.mp3"
    "디지대 대원" "어떻게 할까요? 부반장"
    voice "audio/voice/v1_5_73.mp3"
    f "부하들은 크래커와 마찬가지로 디지몬을 독과 툴로 조작하고 있다."
    voice "audio/voice/v1_5_74.mp3"
    f "이 라스트 코스트와 디지털 월드의 경치도, 가상 모니터의 모식도나 수치로는 관측하고 있으나, 직접 보고 있지도 않고 냄새도 맡고 있지 않다"
    voice "audio/voice/v1_5_75.mp3"
    f "알고는 있지만, 이해하고 있지는 않다.…… 라는 건, 어딘가의 유명한 학자의 말이었던가."

    show hime at Position (xalign=0.5, yalign= -0.2) with dissolve
    voice "audio/voice/v1_5_76.mp3"
    f "알고 있는 것은―― 이 장소에서는 그녀, 부반장 타마히메 사츠키 뿐이다."
    voice "audio/voice/v1_5_77.mp3"
    f "툴로 후각의 99%%를 차단."
    voice "audio/voice/v1_5_78.mp3"
    f "사츠키의 디지몬은 이 라스트 코스트 같은 열악한 환경을 오히려 무척 좋아한다만……."
    hide hime with dissolve

    voice "audio/voice/v1_5_79.mp3"
    hime nomal "경찰은 범죄자를 취향 따라서 고를 수는 없으니…… 전원 체포"
    voice "audio/voice/v1_5_80.mp3"
    f "10 이상의 녹색 점이, 갑자기 가상 모니터의 모식도에 출현했다."
    voice "audio/voice/v1_5_81.mp3"
    f "크래커의 에스피몬들은 진작에 사츠키 휘하의 경찰에게 포위되어 있었던 것이다."
    voice "audio/voice/v1_5_82.mp3"
    hime "놈들의 보이스 채팅에 강제 개입. 동시에, 코만드라몬 분대는 2방향에서 타켓을 제압"
    voice "audio/voice/v1_5_83.mp3"
    "부대원" "라져"
    voice "audio/voice/v1_5_84.mp3"
    f "에스피몬은 이쪽을 눈치채지 못했다."
    voice "audio/voice/v1_5_85.mp3"
    f "크래커들에게는 애당초 보이지 않고, 자신들의 디지몬이 있는 이 장소조차 모르고 있을 터이다."
    voice "audio/voice/v1_5_86.mp3"
    f "그들 크래커에게 보이고 있는 것은 손에 든 디지몬 독의 조악한 액정 화면뿐이다. 그래서 경계하고 있지 않다."
    voice "audio/voice/v1_5_87.mp3"
    f "하지만 그녀―― 사츠키에게는 보인다."
    voice "audio/voice/v1_5_88.mp3"
    f "있는 그대로. 오감으로."
    voice "audio/voice/v1_5_89.mp3"
    f "그녀는 「굴레」를 초월한 자니까."
    voice "audio/voice/v1_5_90.mp3"
    hime "잘・도! 나타났겠다 밀어 크래커 놈들!" with vpunch
    voice "audio/voice/v1_5_91.mp3"
    f "보이스 채팅에 강제 개입, 경고."
    voice "audio/voice/v1_5_92.mp3"
    f "울려 퍼지는 미성을 듣고 에스피몬들이 드디어 이쪽의 존재를 눈치챘다."
    voice "audio/voice/v1_5_93.mp3"
    f "그 때에는 슬그머니 포복 전진하고 있던 사츠키 부하의 디지몬들이 일어서, 밀어꾼들을 포위하고 있었다."
    
    scene bg_chap_1_5_6 with fade
    voice "audio/voice/v1_5_94.mp3"
    f "――코만드라몬 성장기 사이보그형 바이러스종"

    voice "audio/voice/v1_5_95.mp3"
    f "경찰 제식 장비 디지몬이다."
    voice "audio/voice/v1_5_96.mp3"
    f "외견은 용인, 리저드맨이라고 할 법한 모습"
    voice "audio/voice/v1_5_97.mp3"
    f "「POLICE」라고 써진 헬멧과 보디아머를 장비하고 어설트 라이플을 쥐고 있다."
    voice "audio/voice/v1_5_98.mp3"
    f "코만드라몬은 표면에 특수한 텍스처 가공이 되어 있어 주위 환경에 따라 전자전 미채를 입는 것이 가능했다."
    voice "audio/voice/v1_5_99.mp3"
    f "이것으로 적에게 들키지 않고 접근할 수 있다."

    scene bg_chap_1_5_4 with fade
    voice "audio/voice/v1_5_100.mp3"
    "디지대 대원" "디지타마를 발견!"
    voice "audio/voice/v1_5_101.mp3"
    f "코만드라몬이 밀렵된 디지타마를 확보한다."
    voice "audio/voice/v1_5_102.mp3"
    f "도구와, 물건은 진압했다."
    voice "audio/voice/v1_5_103.mp3"
    f "남은 건 리얼의 크래커 본인을 검거하면 3점 세트다. 라는 건 아니다."
    voice "audio/voice/v1_5_104.mp3"
    "크래커1" "――경찰?!" with vpunch
    voice "audio/voice/v1_5_105.mp3"
    "크래커2" "――디지대냐고! 재수도 없네!"
    voice "audio/voice/v1_5_106.mp3"
    f "드디어 사태를 파악한 크래커들이었지만, 보이스 채팅에서 허둥대는 것밖에 할 수 없다."
    voice "audio/voice/v1_5_107.mp3"
    f "사츠키는 현재 시각, 체포 용의를 고했다."
    voice "audio/voice/v1_5_108.mp3"
    hime nomal "――현행범 체포, 순순히 오라를 받아! 말해두겠지만 회선 꼬아서 도망쳐 봤자 헛수고니까……"
    voice "audio/voice/v1_5_109.mp3"
    hime "벌써 파악했어! 경찰 깔보지 마, 너희들 이름이랑 학교도 특정했으니까!"
    voice "audio/voice/v1_5_110.mp3"
    f "지긋지긋하게도 크래커들은 고등학생인 것 같다. 체포가 아니라 보도(補導)일지도 모른다."
    voice "audio/voice/v1_5_111.mp3"
    f "나쁜 선배들에게 꼬드겨져 크래커 놀이로 용돈벌이. 있을 법한 이야기이기는 하다."
    voice "audio/voice/v1_5_112.mp3"
    "크래커2" "체포라니…… 무슨 용의야! 우리가 뭘 했다고……"
    voice "audio/voice/v1_5_113.mp3"
    hime "부정 접속 방지법 및 네트워크 기본법, 디지털 파괴활동 방지법 위반! 쉽게 말하면 디지타마 밀어죄다 이 자식아!"
    voice "audio/voice/v1_5_114.mp3"
    f "사츠키는 무뚝뚝하게 내뱉었다."
    voice "audio/voice/v1_5_115.mp3"
    "크래커2" "여긴…… 디지털 월드라고!"
    voice "audio/voice/v1_5_116.mp3"
    "크래커2" "어느 나라도 아냐! 왜 일본 경찰이 참견하는 거야!"
    voice "audio/voice/v1_5_117.mp3"
    f "과연 크래커 꼬마들은, 약간 지혜가 있어서 포기가 느리다."
    voice "audio/voice/v1_5_118.mp3"
    f "사츠키는 스읍 하고 숨을 들이키고, 내뱉고, 목소리에 가시를 세웠다."
    voice "audio/voice/v1_5_119.mp3"
    hime "네트워크의 자유, 디지털 월드의 자유란 거냐……?"
    voice "audio/voice/v1_5_120.mp3"
    "크래커들" "?!" with vpunch
    voice "audio/voice/v1_5_121.mp3"
    hime "크래커 팀의 이념 말이지……? 참 잘나신 주장이다마는…… 알겠냐, 잠꼬대는 SNS에서나 해!"
    voice "audio/voice/v1_5_122.mp3"
    hime "어금니 잡아 뽑아서 덜덜 떨게 해줄까, 썩어빠진 크래커놈들아!" with vpunch
    voice "audio/voice/v1_5_123.mp3"
    "촤아아아아아아악!"
    voice "audio/voice/v1_5_124.mp3"
    f "수면에서 눈알만 내놓고 잠복해 있던 사츠키의 디지몬이, 잠수함처럼 모습을 드러내었다."

    scene bg_chap_1_5_7 with fade
    voice "audio/voice/v1_5_125.mp3"
    "누메몬" "누메에~~~~~~~~!"
    voice "audio/voice/v1_5_126.mp3"
    f "경광등의 빨간 불빛이 회전한다."
    voice "audio/voice/v1_5_127.mp3"
    f "그 디지몬의 모습, 역겨운 신음소리, 질척한 대박력에 크래커의 에스피몬들은 떨었다."
    voice "audio/voice/v1_5_128.mp3"
    f "사츠키의 디지몬은, 자그마치――"

    scene bg_chap_1_5_4 with fade
    voice "audio/voice/v1_5_129.mp3"
    hime nomal "귓구멍 파고 잘 들어! 리얼의 너희들이 일본국민이고! 위법행위에 손을 담고 있는 한! 일본경찰의 신세를 져서 보호자를 부르게 된다고"
    voice "audio/voice/v1_5_130.mp3"
    hime "귀찮구만 이 자식들…… 어이, 거기 움직이지 마!"
    voice "audio/voice/v1_5_131.mp3"
    f "――「다이배니쉬」!"
    scene bg_chap_1_5_8 with flash
    voice "audio/voice/v1_5_132.mp3"
    f "갑자기 에스피몬이 사라졌다."
    voice "audio/voice/v1_5_133.mp3"
    f "차례차례로, 코만드라몬이 총구 끝의 타겟을 놓친다."
    voice "audio/voice/v1_5_134.mp3"
    f "소실 매직이다. 에스피몬이 배꼽 위치에 있는 버튼을 누른 순간, 라스트 코스트의 배경에 녹아들듯이 사라졌다."
    voice "audio/voice/v1_5_135.mp3"
    hime nomal "광학미채?! 건방지게!"
    voice "audio/voice/v1_5_136.mp3"
    f "투명 망토다."
    voice "audio/voice/v1_5_137.mp3"
    f "일제사격. 코만드라몬들이 어설트 라이플을 쏴갈긴다."
    voice "audio/voice/v1_5_138.mp3"
    f "분대 전력 화력."
    voice "audio/voice/v1_5_139.mp3"
    f "코만드라몬에게 질세라 미채를 감싼 에스피몬은, 하지만, 보기 좋게 경찰의 포위를 빠져나갔다."
    voice "audio/voice/v1_5_140.mp3"
    f "이것은 크래커의 조작은 관계없는, 디지몬 AI의 자기 방위 기능이다."

    voice "audio/voice/v1_5_141.mp3"
    hime "「메카노몬」!"
    voice "audio/voice/v1_5_142.mp3"
    f "사츠키가 지시하자 동시에 등 뒤에서 2체의 디지몬이 더 미채를 풀고 출현한다."
    
    scene bg_chap_1_5_9 with fade
    voice "audio/voice/v1_5_143.mp3"
    f "――메카노몬 머신형 성숙기 바이러스종"
    voice "audio/voice/v1_5_144.mp3"
    f "에스피몬이나 코만드라몬보다 대형 디지몬이다."
    voice "audio/voice/v1_5_145.mp3"
    f "스케일감으로 말하자면 높이 3, 4미터 정도. 보디 컬러는 흰색 베이스. "
    voice "audio/voice/v1_5_146.mp3"
    f "그 외견은 로봇, 팔 부분이 긴 사람 형태 파워드 슈츠 그 자체다."
    voice "audio/voice/v1_5_147.mp3"
    f "디지몬은 서류상 경찰 비품 취급이지만, 메카노몬은 특과(特科)차량으로 분류되어 있었다. "
    voice "audio/voice/v1_5_148.mp3"
    f "내부에는 조종을 맡은 전임 코만드라몬이 탑승해 있다."

    scene bg_chap_1_5_8 with fade
    voice "audio/voice/v1_5_149.mp3"
    "윙 위이잉…………"
    voice "audio/voice/v1_5_150.mp3"
    f "외눈 모노아이가, 번뜩 하고 주변을 살핀다."
    voice "audio/voice/v1_5_151.mp3"
    f "메카노몬은 강력한 탐지기, 각종 센서 등 전자전 장비를 탑재하는 것으로, 현장 지휘차가 될 수 있는 것이다."
    voice "audio/voice/v1_5_152.mp3"
    "치잉――"
    voice "audio/voice/v1_5_153.mp3"
    f "메카노몬의 몸통에 박힌 리니어 렌즈에서 광학병기가 발사되었다."
    voice "audio/voice/v1_5_154.mp3"
    f "――「트윙클 빔」!"
    scene bg_chap_1_5_4 with flash
    voice "audio/voice/v1_5_155.mp3"
    f "레이저 광선이 보이지 않는 에스피몬 1체를 관통했다."
    voice "audio/voice/v1_5_156.mp3"
    f "파직파직 하고 불꽃을 흩뿌리며 광학미채가 풀리며, 에스피몬은 번쩍번쩍 춤추듯이..."
    voice "audio/voice/v1_5_157.mp3"
    f "사철을 말아올리며 해안에 쓰러졌다."
    voice "audio/voice/v1_5_158.mp3"
    f "가상 모니터에 남은 3개의 빨간 점은 사라지듯 점멸하며 뿔뿔이."
    voice "audio/voice/v1_5_159.mp3"
    hime nomal  "놓치지 마! 쏴!"
    voice "audio/voice/v1_5_160.mp3"
    "디지대 대원" "다음 탄 차지 중…… 전부 다 포착할 수는 없습니다!"
    voice "audio/voice/v1_5_161.mp3"
    f "사츠키와 메카노몬에 탄 부하가 교신한다, 그 때,"

    with flash
    voice "audio/voice/v1_5_162.mp3"
    show lighting at Position(xalign = 0.5, yalign = 1.0) with vpunch
    hide lighting with flash
    "?" "――「쁘띠 임펄스」!" with vpunch

    voice "audio/voice/v1_5_163.mp3"
    f "뇌명과 함께, 라스트 코스트에 번개의 묶음이 내리꽂혔다."

    voice "audio/voice/v1_5_164.mp3"
    f "예상치 못한 사태에 사츠키의 판단이 늦어진다."
    voice "audio/voice/v1_5_165.mp3"
    hime "…………?! 에스피몬이!"
    voice "audio/voice/v1_5_166.mp3"
    f "경찰 무선이 어지러이 오간다."

    with flash
    voice "audio/voice/v1_5_167.mp3"
    "파지지지직" with vpunch
    voice "audio/voice/v1_5_168.mp3"
    f "숯검정이 된 에스피몬들이 차례차례로 낙하해 대파됐다."
    voice "audio/voice/v1_5_169.mp3"
    f "번개 창이 남은 3체의 에스피몬을 동시에, 정확하게 꿰뚫은 것이다."
    voice "audio/voice/v1_5_170.mp3"
    f "누구냐……?!"
    voice "audio/voice/v1_5_171.mp3"
    f "사츠키는 헤드업 가상 모니터에 출현한 새로운 마커를 찾았다."

    scene bg_chap_1_5_11 with fade
    voice "audio/voice/v1_5_172.mp3"
    f "그 녀석은, 아무렇지도 않은 듯 서 있었다."
    voice "audio/voice/v1_5_173.mp3"
    f "기능 정지한 에스피몬의 위에."

    voice "audio/voice/v1_5_174.mp3"
    f "그 모습은, 마치 전설의 뇌수(雷獣)인가."
    voice "audio/voice/v1_5_175.mp3"
    hime nomal "저건 「펄스몬」……?!" with vpunch

    scene bg_chap_1_5_12 with fade
    voice "audio/voice/v1_5_176.mp3"
    f "――펄스몬 성장기 수인형 백신종"
    voice "audio/voice/v1_5_177.mp3"
    f "「전광석화」――그 이명대로 지그재그로 고속 이동하는 디지몬의 모습은, 눈으로 포착하는 것조차 힘들다."

    scene bg_chap_1_5_11 with fade
    voice "audio/voice/v1_5_178.mp3"
    f "새로운 크래커인가."
    voice "audio/voice/v1_5_179.mp3"
    f "코만드라몬 분대가 총구를 돌렸다."
    voice "audio/voice/v1_5_180.mp3"
    hime nomal "펄스몬을 쓰는 녀석은, 내가……"
    voice "audio/voice/v1_5_181.mp3"
    f "사츠키는 그 녀석의 이름을 알고 있었다."
    voice "audio/voice/v1_5_182.mp3"
    hime "경찰이 알고 있는 한 한명뿐이다. 그 녀석은…… 해커!"
    voice "audio/voice/v1_5_183.mp3"
    "디지대 대원" "부반장님! 지시를!"
    voice "audio/voice/v1_5_184.mp3"
    hime "해커「저지」인가!"

    with flash
    voice "audio/voice/v1_5_185.mp3"
    "파지직" with vpunch
    voice "audio/voice/v1_5_186.mp3"
    f "힐끔 사츠키의 디지몬을 흘겨본 펄스몬은"
    voice "audio/voice/v1_5_187.mp3"
    pul "마무리가 허술하네, 디지대 부반장 씨"

    scene bg_chap_1_5_8 with flash
    voice "audio/voice/v1_5_188.mp3"
    show lighting2 at Position(xalign=-0.5, yalign=0.4) with vpunch
    hide lighting2 with flash
    f "미소와 손가락 키스를 던지고, 홀연히 네트워크의 바다로 번개처럼 뛰어 사라졌다."
    voice "audio/voice/v1_5_189.mp3"
    hime nomal "저……! 머리 끝까지 화났다~~~~!"
    voice "audio/voice/v1_5_190.mp3"
    "디지대 대원" "부반장님!"
    voice "audio/voice/v1_5_191.mp3"
    f "코만드라몬 분대가 지시를 재촉한다."
    voice "audio/voice/v1_5_192.mp3"
    f "사츠키는 업신여겨진 분노로 내심 부들부들 떨고 있었지만, 현장 지휘관으로서 어떻게든 평정을 되찾았다."
    voice "audio/voice/v1_5_193.mp3"
    hime "에스피몬을 제압…… 밀렵된 디지타마를 확보. 리얼에 관한 건 앞으론 관할부서에 맡겨"
    voice "audio/voice/v1_5_194.mp3"
    "디지대 대원" "저 펄스몬은……"
    voice "audio/voice/v1_5_195.mp3"
    hime "웃기지도 않는 해커 자식은 냅둬. 어차피 따라잡을 수도 없어. 놈도……"
    voice "audio/voice/v1_5_196.mp3"
    f "사츠키는 부루퉁해졌다."
    voice "audio/voice/v1_5_197.mp3"
    f "펄스몬…… 저것과 링크한 해커도 사츠키와 「동류」다."
    voice "audio/voice/v1_5_198.mp3"
    f "――「굴레」를 초월한 자."
    voice "audio/voice/v1_5_199.mp3"
    "디지대 대원" "라져, 부반장님"
    voice "audio/voice/v1_5_200.mp3"
    hime "미안, K라인―― 경고 기준치를 넘을 것 같아. 타임 리미트…… 어기면 반장이 시끄럽게 굴고, 페널티로 감봉당하고"
    voice "audio/voice/v1_5_201.mp3"
    "디지대 대원" "네, 먼저 돌아가십시오! 그리고 디지타마 말입니다만……"
    voice "audio/voice/v1_5_202.mp3"
    f "부하가 빠른 말로 보고했다."
    voice "audio/voice/v1_5_203.mp3"
    hime "?!" with vpunch
    voice "audio/voice/v1_5_204.mp3"
    f "사츠키는 드디어 손쓸 수 없을 정도로 기분이 나빠졌다."
    voice "audio/voice/v1_5_205.mp3"
    f "방금 전까지 해안에 굴러다니고 있었을 터인 디지타마가, 없어져 있었던 것이다."
    voice "audio/voice/v1_5_206.mp3"
    f "잽싸게 집어간 것은, 물론……."
    voice "audio/voice/v1_5_207.mp3"
    f "그야말로「전광석화」――"
    voice "audio/voice/v1_5_208.mp3"
    hime "펄스몬…… 해커 저지! 증거품 내놔, 이 자식아~~~~!" with vpunch
    
    "Chapter 1-5 End..." with Pause(20)
# 챕터 1-6 시작
label Chapter1_6:

    scene black with blinds
    scene bg_chap_1_6 with blinds

    voice "audio/voice/v1.mp3"
    "Chapter1-6" "Eiji: Wolf of ninth avenue" 
    
    voice "audio/voice/v1_6_1.mp3"
    f "크래커 팽, 나가스미 에이지는"

    voice "audio/voice/v1_6_2.mp3"
    f "클라이언트인 어바딘 일렉트로닉스(AE사) 덴린구 디지털 라보(DDL)의 류센지 교수를 방문했다."

    voice "audio/voice/v1_6_3.mp3"
    f "거기서 최신형 디지몬 독 디지몬 링커와 함께 1체의 디지몬을 받는다."

    voice "audio/voice/v1_6_4.mp3"
    f "역 앞 가게에서 규동에 고기랑 달걀을 추가한 것을 테이크아웃해서, 에이지는 오랜만에 기분 좋게 귀가길에 올랐다."

    scene black with blinds
    scene bg_chap_1_6_1 with blinds

    voice "audio/voice/v1_6_5.mp3"
    "따-잉"

    voice "audio/voice/v1_6_6.mp3"
    f "불구(仏具) 종을 울린다"

    voice "audio/voice/v1_6_7.mp3"
    f "자취하는 무척이나 좁은 원룸(다다미 3장) 복층 구조에 목제 불단, 불은 LED다."

    voice "audio/voice/v1_6_8.mp3"
    f "화재가 날 수도 있으니 평소에 향은 피우지 않는다."

    voice "audio/voice/v1_6_9.mp3"
    e "응, 다녀왔어. 아빠, 엄마, 할아버지랑 할머니도"

    voice "audio/voice/v1_6_10.mp3"
    f "덤으로 개도."

    voice "audio/voice/v1_6_11.mp3"
    f "위패에는 가족들의 판이 함께 들어있다."

    voice "audio/voice/v1_6_12.mp3"
    f "어째선지 옛날에 길렀던 개의 몫도 있다."

    voice "audio/voice/v1_6_13.mp3"
    f "손을 맞대고, 에이지는 탁자에서 혼자 저녁을 먹었다."

    scene black with blinds
    scene bg_chap_1_6_2 with blinds

    voice "audio/voice/v1_6_14.mp3"
    f "팔의 디지몬 링커를 본다."

    voice "audio/voice/v1_6_15.mp3"
    e "본 적 없는 디지몬이구나- 너"

    voice "audio/voice/v1_6_16.mp3"
    f "루가몬."

    voice "audio/voice/v1_6_17.mp3"
    f "컬러 액정에는 개와 같은 디지몬이 몸을 둥글게 말고 있었다."
    
    scene black with fade
    show ryusenji at Position(xalign = 0.5, yalign = -0.2) with dissolve
    voice "audio/voice/v1_6_18.mp3"
    ryusenji "――이 디지몬을 육성해주었으면 한다."
    
    
    scene bg_chap_1_6_2 with fade
    voice "audio/voice/v1_6_19.mp3"
    f "류센지에게서 받은 의뢰는, 지극히 심플했다."

    voice "audio/voice/v1_6_20.mp3"
    f "GriMM을 들여다보면 디지타마 육성 일은 금방 눈에 띈다."

    voice "audio/voice/v1_6_21.mp3"
    f "애완동물로 말하자면 브리더."

    voice "audio/voice/v1_6_22.mp3"
    f "일종의 학습형 AI 프로그램인 디지몬의 성장은 탄생부터의 패턴이 크게 관계한다고 한다."

    voice "audio/voice/v1_6_23.mp3"
    f "그렇다면 디지몬을 다루는 전문가인 크래커가 브리더를 겸하는 일도 있다는 것이다."

    scene black with fade
    show ryusenji at Position(xalign = 0.5, yalign = -0.2) with dissolve
    voice "audio/voice/v1_6_24.mp3"
    ryusenji "――내 연구에 관심이 있다면. 루가몬과의 만남은, 자네에게 있어서 무척이나 흥미로운 것이 될 것일세."
    
    scene bg_chap_1_6_2 with fade
    voice "audio/voice/v1_6_25.mp3"
    e "그 류센지 교수에게 그렇게까지 기대를 받는다면 할 수밖에 없지!"

    voice "audio/voice/v1_6_26.mp3"
    f "인생에서 이렇게 흥분한 적은 없었다."

    voice "audio/voice/v1_6_27.mp3"
    f "어쨌든 간에 그 사람을 따라간다면 틀림없다."

    voice "audio/voice/v1_6_28.mp3"
    f "그렇다고는 해도, 에이지는 디지몬 육성 경험이 그다지 없었다."

    voice "audio/voice/v1_6_29.mp3"
    e "티라노몬이 3체 있지만, 하고 있는 건 툴 조정…… 튜닝이니까 말야."

    voice "audio/voice/v1_6_30.mp3"
    e "그것도 육성이라고 한다면 그렇긴 한데"

    voice "audio/voice/v1_6_31.mp3"
    f "탁자에다 소유중인 디지몬 독을 늘어놓는다."

    show gadget at Position(xalign = 0.5,yalign = 0.35) with dissolve
    voice "audio/voice/v1_6_32.mp3"
    f "흑백 액정 화면에 도트 그림의 티라노몬이 비춰지고 있었다."

    voice "audio/voice/v1_6_33.mp3"
    f "격납하고 있는 것은 손바닥에 들어올 사이즈의 독이다."

    voice "audio/voice/v1_6_34.mp3"
    f "이 타입은 스펙적으로는 구식이지만"

    voice "audio/voice/v1_6_35.mp3"
    f "설계도가 나돌아다니고 있어서 파츠가 비교적 입수하기 쉬워 자작하기 쉽다."

    voice "audio/voice/v1_6_36.mp3"
    f "GriMM의 크래커 지향 샵에서는 전용 조립 세트, 완성품이 거래되고 있었다."

    voice "audio/voice/v1_6_37.mp3"
    f "에이지도 몇 개인가 소유하고 있다."

    voice "audio/voice/v1_6_38.mp3"
    e "납품용 독은 교수님이 메모리 영역이 망가져 있다고 했던가…… "

    voice "audio/voice/v1_6_39.mp3"
    e "파츠 교환하야겠네."

    voice "audio/voice/v1_6_40.mp3"
    e "뭐, 디지몬 링커가 있으니까 당분간은 괜찮나"

    hide gadget with dissolve

    voice "audio/voice/v1_6_41.mp3"
    f "팔에 채워진 신품 디지몬 링커를 보고, 에이지는 떠올랐다는 듯이 씩 웃었다."

    voice "audio/voice/v1_6_42.mp3"
    f "이 루가몬은 에이지에게 있어서 마치 행운의 사자다."

    voice "audio/voice/v1_6_43.mp3"
    f "소중하게 여겨야지…… 그렇게 생각이 들었다."

    voice "audio/voice/v1_6_44.mp3"
    e "――그렇다고 해도, 샤워할 때도 24시간 디지몬 링커를 차고 있으라니, 어떻게 된 거지……?"

    voice "audio/voice/v1_6_45.mp3"
    f "완전방수, 항균 사양이니까 문제는 없는 것 같지만……."

    voice "audio/voice/v1_6_46.mp3"
    f "에이지가 새로운 가제트의 조작을 외우는 2, 3일 동안에도 루가몬은 성장했다."

    voice "audio/voice/v1_6_47.mp3"
    f "디지몬 링커로 에이지의 고동을 느끼면서, 쑥쑥 자라는 디지몬."

    voice "audio/voice/v1_6_48.mp3"
    e "뭐랄까 가슴에 품고 기른 내 아이란 느낌이네~"

    voice "audio/voice/v1_6_49.mp3"
    f "에이지는 손목시계 안의 디지몬을 사랑스럽게 바라보았다."

    show devo at Position(xalign = 0.5,yalign = 0.3) with dissolve
    voice "audio/voice/v1_6_50.mp3"
    f "디지몬의 성장―― 진화는 체계화되어 있다."

    voice "audio/voice/v1_6_51.mp3"
    f "디지타마에서 부화하면 우선 유년기 스테이지로 나아간다."

    voice "audio/voice/v1_6_52.mp3"
    f "이것은 디지몬의 아기다."

    voice "audio/voice/v1_6_53.mp3"
    f "아직 학습하지 않아서 곧바로는 툴로 유용하게 사용할 수는 없다."

    voice "audio/voice/v1_6_54.mp3"
    f "보통은 이 유년기 단계에서 디지몬 육성이 시작하는 것이지만."

    voice "audio/voice/v1_6_55.mp3"
    f "루가몬은 이미 다음 스테이지인 성장기다."

    hide devo with dissolve

    # 휴대폰 사용 이미지 추가 필요
    #
    #

    voice "audio/voice/v1_6_56.mp3"
    f "에이지는 GriMM에서 브리더들에게 질문을 올렸다."

    voice "audio/voice/v1_6_57.mp3"
    f "물론 류센지에게서 받은 일에 관한 것, 루가몬에 관한 것은 말하지 않고, 일반적인「개를 닮은」디지몬의 육성법에 대해……."

    voice "audio/voice/v1_6_58.mp3"
    f "애당초 루가몬에 관한 건 GriMM을 검색해봐도 전혀 HIT하지 않았던 것이다."

    voice "audio/voice/v1_6_59.mp3"
    e "AI학습용 프로그램, 트레이닝 프로그램…… 여러가지 있는걸"

    voice "audio/voice/v1_6_60.mp3"
    f "약간 귀찮을지도."

    voice "audio/voice/v1_6_61.mp3"
    f "이제와서 에이지는 후회했다."

    voice "audio/voice/v1_6_62.mp3"
    e "펫 기르는 게 얼마만이지."

    voice "audio/voice/v1_6_63.mp3"
    e "어렸을 적에 길렀던 개가 죽고 난 이래인가"

    voice "audio/voice/v1_6_65.mp3"
    f "――디지털 월드의 존재방식, 디지몬의 존재방식을, 이 눈으로, 직접 보는 것."

    voice "audio/voice/v1_6_66.mp3"
    f "가상 모니터와 관측 데이터가 아닌"

    voice "audio/voice/v1_6_67.mp3"
    f "인간의 오감으로 직접 디지털 월드를 파악하는 것."

    voice "audio/voice/v1_6_68.mp3"
    f "류센지는 그런 굉장한 연구를 하고 있는 선생님이다."

    voice "audio/voice/v1_6_69.mp3"
    e "그런 게 가능하다면 보고 싶은걸."

    voice "audio/voice/v1_6_70.mp3"
    e "나도, 류센지 교수님이 보고 있는 세계를."

    voice "audio/voice/v1_6_71.mp3"
    e "디지몬이 살고 있는 세계…… 인가."

    voice "audio/voice/v1_6_72.mp3"
    e "루가몬…… 너를 길러내면, 완전체나 궁극체까지 진화시키면 뭔가 알 수 있는 걸까?"

    voice "audio/voice/v1_6_73.mp3"
    f "리얼월드와 디지털 월드의 「굴레」를 초월한다."

    voice "audio/voice/v1_6_74.mp3"
    f "류센지가 말한 것처럼, 그런 초 일류 크래커가 될 수 있다면."

    voice "audio/voice/v1_6_75.mp3"
    f "알림이 왔다."

    voice "audio/voice/v1_6_76.mp3"
    f "스마트폰을 손에 든다." 

    voice "audio/voice/v1_6_77.mp3"
    f "GriMM에서 질문한 것에 답변이 달린 모양이다."

    voice "audio/voice/v1_6_78.mp3"
    "답글" "――팽, 디지몬 육성 데뷔 축하해!"

    voice "audio/voice/v1_6_79.mp3"
    "답글" "성장기부터 육성하는 거라면 다른 디지몬이랑 같이 다수 육성을 추천해."

    voice "audio/voice/v1_6_80.mp3"
    "답글" "2체 이상 있으면 알아서 놀면서 점점 학습해 가니까 말야."

    voice "audio/voice/v1_6_81.mp3"
    e "과연, 디지몬 다수 육성인가! 과연 집합지성!"

    voice "audio/voice/v1_6_82.mp3"
    f "에이지는 바로 티라노몬이 든 독을 디지몬 링커에 접속시켰다."

    voice "audio/voice/v1_6_83.mp3"
    f "최신형 디지몬 링커에는 충분하고도 남을 정도의 용량과 처리능력이 있었다."

    voice "audio/voice/v1_6_84.mp3"
    f "루가몬을 티라노몬들과 같이 두면 되겠지."

    voice "audio/voice/v1_6_85.mp3"
    f "하지만…… 에이지는 깜빡, 그 답변의 뒷 내용을 읽지 않았다."

    voice "audio/voice/v1_6_86.mp3"
    "답글" "――디지몬에 따라서는 개랑 마찬가지로 무리의 서열을 중요시하니까."

    voice "audio/voice/v1_6_87.mp3"
    "답글" "훈육은 처음이 중요해!"

    voice "audio/voice/v1_6_88.mp3"
    f "그렇게 해서……."

    voice "audio/voice/v1_6_89.mp3"
    f "며칠 후, 큰일이 일어나 버렸다."

    show bg_chap_1_6_3 with fade

    "Chapter 1-6 End..." with Pause(20)
# 챕터 1-7 시작
label Chapter1_7:

    scene black with blinds
    scene bg_chap_1_7 with blinds

    voice "audio/voice/v1.mp3"
    "Chapter1-7" "Eiji: Wolf of ninth avenue" 

    
    scene black with blinds
    scene bg_chap_1_2_4 with blinds

    voice "audio/voice/v1_7_1.mp3"
    f "어바딘 일렉트로닉스 덴린구 디지털 라보."

    voice "audio/voice/v1_7_2.mp3"
    f "긴급 연락을 받은 에이지는 바로 DDL로 나가 오피스에서 울상을 지었다."

    voice "audio/voice/v1_7_3.mp3"
    e nomal "교수님~! 류센지 교수님~!" with vpunch

    show ryusenji at Position(xalign = 0.5,yalign = -0.2) with dissolve
    voice "audio/voice/v1_7_4.mp3"  
    ryusenji "안녕, 에이지 군"

    voice "audio/voice/v1_7_5.mp3"  
    f "이미 오후지만, 류센지는 항상 「안녕(おはよう)」이라고 하는 타입인 듯하다."

    voice "audio/voice/v1_7_6.mp3"  
    e "뭐에요, 이 디지몬은!" with vpunch

    voice "audio/voice/v1_7_7.mp3"  
    f "디지몬 링커의 화면에서 루가몬이 낮잠을 자고 있었다."

    voice "audio/voice/v1_7_8.mp3"  
    f "배가 부른 것인지, 좋은 꿈을 꾸고 있는 듯하다."

    voice "audio/voice/v1_7_9.mp3"  
    ryusenji "육성은 순조로운 것 같군. 진화하는 게 기대되는걸"

    voice "audio/voice/v1_7_10.mp3"  
    f "류센지는 빙긋 웃었다."

    voice "audio/voice/v1_7_11.mp3" 
    f "디지몬은 성장에 따라 모습을 바꾸어 간다."
    hide ryusenji with dissolve

    show devo at Position(xalign = 0.5,yalign = 0.3) with dissolve
    voice "audio/voice/v1_7_12.mp3"
    f "디지타마＞유년기(I・II)＞성장기＞성숙기＞완전제＞궁극체"

    voice "audio/voice/v1_7_13.mp3"
    f "예를 들어 곤충이 알아서 애벌레, 번데기, 성충이 되듯이."

    voice "audio/voice/v1_7_14.mp3"  
    f "다른 점은, 같은 개체가 전혀 다른 디지몬으로 변화해 가는 것."

    voice "audio/voice/v1_7_15.mp3"  
    f "그래서 디지몬의 성장을 가리켜 학술적으로 굳이 「진화」라고 호칭하고 있다."

    hide devo with dissolve

    show ryusenji at Position(xalign = 0.5,yalign = -0.2) with dissolve
    voice "audio/voice/v1_7_16.mp3"  
    ryusenji "――성숙기로 진화하면 인센티브를 지불하지"

    voice "audio/voice/v1_7_17.mp3"  
    e "인센티브…… 추가보수!" with vpunch

    voice "audio/voice/v1_7_18.mp3"  
    ryusenji "완전체, 설마 했던 궁극체까지 되면 더 둠뿍 내지."

    voice "audio/voice/v1_7_19.mp3"  
    ryusenji "루가몬은 어떤 디지몬으로 진화하려나."

    voice "audio/voice/v1_7_20.mp3" 
    ryusenji "에이지 군과 루가몬의 멋진 모습이 보고 싶은걸" 

    voice "audio/voice/v1_7_21.mp3"  
    f "류센지는 알기 쉽게 에이지를 응원했다."

    voice "audio/voice/v1_7_22.mp3"  
    e "보고 싶은걸…… 이 아니라요! 돈다발의 폭력으로 이야기를 돌리지 말아주세요, 못된 어른이시네"

    voice "audio/voice/v1_7_23.mp3"  
    ryusenji "흠"

    voice "audio/voice/v1_7_24.mp3"  
    e "보셨죠, 어제 보냈던 육성 레포트!"

    voice "audio/voice/v1_7_25.mp3"  
    f "에이지는 항의했다."

    voice "audio/voice/v1_7_26.mp3" 
    ryusenji "내 메일박스에는 매일 수백 수천의 메일이 오네. 실은 거의 열어보지 않는다만"

    voice "audio/voice/v1_7_27.mp3"  
    f "류센지는 시치미를 떼고 말했다."

    voice "audio/voice/v1_7_28.mp3"  
    e "그런 걸 전부 체크하고 있다가는 날이 저물겠지요……"

    voice "audio/voice/v1_7_29.mp3"  
    ryusenji "그 말대로네. 나는 연구자이며, 연구 이외에 돌릴 시간은 없어. 하지만……"

    voice "audio/voice/v1_7_30.mp3"  
    ryusenji "에이지 군에게서 온 연락만은 알림을 설정해두고 체크하고 있지"

    voice "audio/voice/v1_7_31.mp3"  
    e "왠지 가슴이 꽈악 조여오네요"

    voice "audio/voice/v1_7_32.mp3"  
    f "에이지는 자기 가슴을 끌어안았다."

    voice "audio/voice/v1_7_33.mp3"  
    ryusenji "에이지 군은, 나의 소중한 일 상대니까"

    voice "audio/voice/v1_7_34.mp3"  
    f "교수는 이런 점을 미워할 수가 없다."

    voice "audio/voice/v1_7_35.mp3"  
    f "그렇달까 좋아하게 되어 버린다."

    voice "audio/voice/v1_7_36.mp3"  
    f "디지털 월드의 세계적 권위자가, 크래커 젊은이에 지나지 않는 에이지를 일 상대라고 말해준다."

    voice "audio/voice/v1_7_37.mp3"  
    f "에이지의 보고서를 모니터에 펼쳐놓고, 류센지는 첨부된 영상 파일을 재생했다."

    hide ryusenji with dissolve

    show loo_windows at Position (xalign = 0.5, yalign =0.25) with dissolve

    voice "audio/voice/v1_7_38.mp3"
    f "――루가몬 성장기 마수형 바이러스종"  

    hide loo_windows with dissolve

    show loo_windows2 at Position (xalign = 0.5, yalign = 0.25) with dissolve
    voice "audio/voice/v1_7_39.mp3"  
    f "가상 육성 케이지다. 영상의 날짜는 어제."

    voice "audio/voice/v1_7_40.mp3"  
    f "루가몬이 먹이를 먹고 있다."

    voice "audio/voice/v1_7_41.mp3"  
    f "디지몬은 먹이를 먹지 않으면 성장을 멈춰 버린다."

    voice "audio/voice/v1_7_42.mp3"  
    f "그래서 공복이 되면 본능적으로 먹이를 계속해서 먹는다."

    voice "audio/voice/v1_7_43.mp3"  
    f "AI에게 식사라니 기묘하게 느껴지지만, 먹이란 말하자면 데이터이며 정보다."

    voice "audio/voice/v1_7_44.mp3"  
    f "인간 역시 책을 읽거나 영상을 보거나, 공부해서 정보를 얻지 않으면 아무리 해도 성장하지 않을 것이다."

    voice "audio/voice/v1_7_45.mp3"  
    f "루가몬의 앞에는, 어째선지 먹이 그릇이 4개."

    voice "audio/voice/v1_7_46.mp3"  
    f "케이지 구석에는, 다수 육성을 하고 있던 3체의 티라노몬이 어떻게 된 일인지 덜덜 떨고 있었다."

    voice "audio/voice/v1_7_47.mp3"  
    ryusenji nomal "――티라노몬으로는 3체나 있어도 버거운가"

    voice "audio/voice/v1_7_48.mp3"  
    f "류센지는 흥미 깊은 듯이 체크했다."

    voice "audio/voice/v1_7_49.mp3"  
    e "티라노몬은 성숙기인데. 한단계 아래 성장기인 루가몬에게 이렇게 되어 버리다니……"

    voice "audio/voice/v1_7_50.mp3"  
    ryusenji "루가몬은 마수형, 그 중에서도 늑대의 데이터에 강한 영향을 받고 있지"

    voice "audio/voice/v1_7_51.mp3"  
    f "류센지가 설명했다."

    voice "audio/voice/v1_7_52.mp3"  
    e nomal "늑대…… 저거, 개가 아니었구나"

    voice "audio/voice/v1_7_53.mp3" 
    f "에이지는 머리를 긁적였다."

    voice "audio/voice/v1_7_54.mp3"  
    ryusenji "개라고 한다면 개다만…… 좀 더 원시적, 늑대를 길들인 것의 자손이 개일세."

    voice "audio/voice/v1_7_55.mp3"  
    ryusenji "어쨌든 간에 무리를 짓고 보스가 존재하지."

    voice "audio/voice/v1_7_56.mp3"  
    ryusenji "무리 내에서의 순위 매기기에 엄격하네"

    voice "audio/voice/v1_7_57.mp3"  
    e "그럼…… 같은 케이지에서 길렀으니까? 루가몬 녀석 티라노몬을…… 부하로 삼았다고요?!"

    voice "audio/voice/v1_7_58.mp3"  
    ryusenji "그런 듯하군. 먹이는 물론 보스가 우선이지"

    voice "audio/voice/v1_7_59.mp3"  
    f "류센지는 어째선지 미소짓고 있었다."

    voice "audio/voice/v1_7_60.mp3"  
    e "그렇다고 남의 먹이까지 먹다니, 이 먹보! 아니 처음에는 티라노몬 째로 먹으려고 했다고요, 이녀석!"

    voice "audio/voice/v1_7_61.mp3"  
    ryusenji "호오! 그거 흥미롭군. 그야말로 거신(巨神)마저 먹어치우는 신화 속 마랑(魔狼)과 같이인가"

    voice "audio/voice/v1_7_62.mp3"  
    e "아무리 그래도 너무 호러여서 영상은 안 찍었어요…… 그보다, 이 녀석 먹이 너무 많이 먹어! 코스트 너무 무거워! 똥도 너무 많이 싸!"

    voice "audio/voice/v1_7_63.mp3"  
    ryusenji "…………그래서"

    voice "audio/voice/v1_7_64.mp3"  
    e "네?"

    voice "audio/voice/v1_7_65.mp3"  
    ryusenji "무슨 문제가 있는 건가?"

    voice "audio/voice/v1_7_66.mp3"  
    f "류센지에게 반대로 질문을 받아 버렸다."

    voice "audio/voice/v1_7_67.mp3"  
    f "과연……"

    voice "audio/voice/v1_7_68.mp3"  
    f "천재 연구자에게 있어서, 이것만으로는 흥미로운 일밖에 되지 않는다."

    voice "audio/voice/v1_7_69.mp3"  
    f "에이지는 한숨을 쉬었다."

    voice "audio/voice/v1_7_70.mp3"  
    e "루가몬을 벤치마크 돌린 결과가, 다음의…… 그 데이터에요."

    voice "audio/voice/v1_7_71.mp3"  
    e "확실히 일반적인 성장기의 스코어는 아니에요"

    voice "audio/voice/v1_7_72.mp3" 
    ryusenji "흠" 

    voice "audio/voice/v1_7_73.mp3" 
    e "그런데 교수님…… 루가몬의 이마에 있는 거, 뭔가요, 저거……" 

    hide loo_windows2 with dissolve

    show loo_windows3 at Position (xalign = 0.5, yalign = 0.25) with dissolve

    voice "audio/voice/v1_7_74.mp3" 
    f "에이지는 영상을 일시정지, 확대했다." 

    voice "audio/voice/v1_7_75.mp3"  
    f "루가몬의 이마에서 코에 걸쳐서 면갑(面甲), 프로텍터가 달려 있었지만. "

    voice "audio/voice/v1_7_76.mp3"  
    f "그 이마의 부분에 반짝이는 보석 같은 것이 박혀 있다."

    voice "audio/voice/v1_7_77.mp3"  
    e "――뭔가 신경쓰인다고 해야 하나. 빛나거나 그럴 때도 있고"

    voice "audio/voice/v1_7_78.mp3"  
    ryusenji "뭐라고도 할 수 없겠군. 하지만 에이지 군, 자네의 착안점은 날카로워"

    voice "audio/voice/v1_7_79.mp3"  
    e "그쵸-"

    voice "audio/voice/v1_7_80.mp3"  
    ryusenji "사용감은? 이미, 사용해 봤겠지"

    voice "audio/voice/v1_7_81.mp3"  
    e "너무 피키해서 AI툴로서의 성능은 평가 불능이에요"

    voice "audio/voice/v1_7_82.mp3"  
    f "에이지는 보류했다."

    voice "audio/voice/v1_7_83.mp3"  
    ryusenji "즉?"

    voice "audio/voice/v1_7_84.mp3"  
    e "툴의 커맨드가 통하지 않는달까…… 말하는 걸 안 듣는다고요, 이녀석! 알은커녕, 산책도 못한다고요."

    voice "audio/voice/v1_7_85.mp3"  
    e "그러고 보니 옛날에 길렀던 개도 산책 나갔을 때 제멋대로 쭉쭉 나가버리는 타입이었지만"

    voice "audio/voice/v1_7_86.mp3" 
    ryusenji "…………. 기를 자신이 없다고?" 

    voice "audio/voice/v1_7_87.mp3"  
    e "설마요! 기를 거에요, 일이고…… 루가몬에 흥미도 있고! 반드시 진화시켜 보이겠어요!"

    voice "audio/voice/v1_7_88.mp3"  
    ryusenji "홀로라이즈시켜 보게"

    voice "audio/voice/v1_7_89.mp3" 
    f "류센지가 말했다." 

    voice "audio/voice/v1_7_90.mp3"  
    f "에이지는 디지몬 링커에서 커맨드를 고른다."

    hide loo_windows3 with dissolve

    voice "audio/voice/v1_7_90_1.mp3"
    "삑 삑...지이잉"
    
    show loo_windows4 at Position (xalign = 0.5, yalign = 0.25) with dissolve # 추후 이미지 변경 필요 
    voice "audio/voice/v1_7_91.mp3"  
    f "자고 있는 루가몬이 그대로 홀로라이즈했다."

    voice "audio/voice/v1_7_92.mp3"  
    f "복슬복슬하고, 크다."

    voice "audio/voice/v1_7_93.mp3"  
    f "성장기 디지몬은, 물론 종류에 따라 다르지만, 대체로 체장 1미터 정도 사이즈다."

    voice "audio/voice/v1_7_94.mp3"  
    f "루가몬도 허스키견이라던가, 그야말로 소형 늑대 정도의 크기다."

    voice "audio/voice/v1_7_95.mp3"  
    f "디지몬 자체가 땅딸막한 포름(forme)이라서, 실내에 있으면 존재감이 있다."

    voice "audio/voice/v1_7_96.mp3"  
    f "털은 블루 그레이, 푸른 늑대다. 눈동자는 레드."

    voice "audio/voice/v1_7_97.mp3"  
    f "할 수만 있다면, 푹신푹신 묻혀보고 싶다."

    voice "audio/voice/v1_7_98.mp3"  
    ryusenji "그 디지몬 링커는 24시간, 에이지 군의 생체정보를 체크하고 있지."

    voice "audio/voice/v1_7_99.mp3"  
    ryusenji "루가몬의 성장 정보와 맞추어 데이터를 검증해 봤는데…… "

    voice "audio/voice/v1_7_99_1.mp3"
    ryusenji "실로!" with vpunch

    voice "audio/voice/v1_7_100.mp3"  
    f "류센지는 큰 목소리를 냈다."

    voice "audio/voice/v1_7_101.mp3"  
    e "왁? 깜짝 놀랐네" with vpunch

    voice "audio/voice/v1_7_102.mp3"  
    ryusenji "실로 훌륭해!"

    voice "audio/voice/v1_7_103.mp3"  
    f "류센지는 대절찬했다."

    voice "audio/voice/v1_7_104.mp3"  
    e "...? 갑자기 칭찬받았다"

    voice "audio/voice/v1_7_104_1.mp3"
    ryusenji "이 수치를 보게나!"

    hide loo_windows4 with dissolve

    show loo_windows5 at Position (xalign = 0.5, yalign = 0.25) with dissolve
    voice "audio/voice/v1_7_105.mp3"  
    f "류센지는 평가 레포트를 표시하고, 흥분해서 화면을 가리켰다."

    voice "audio/voice/v1_7_106.mp3"  
    e "「DS치」……? 그보다, 못 읽겠는데요"

    voice "audio/voice/v1_7_107.mp3"  
    f "수치에 블라인드가 쳐져 있다. 크래커 업계에서도 들어본 적 없는 용어다만……."

    voice "audio/voice/v1_7_108.mp3"  
    ryusenji "그건 D4일세"

    voice "audio/voice/v1_7_109.mp3" 
    e "아, 기밀"

    voice "audio/voice/v1_7_110.mp3" 
    ryusenji "내가 설계한 디지몬과의 상성을 가리키는 하나의 지표네." 

    voice "audio/voice/v1_7_111.mp3"  
    ryusenji "에이지 군…… 자네와 루가몬의 상성만은 이미 일류 크래커에도 뒤지지 않아"

    voice "audio/voice/v1_7_112.mp3"  
    e "진짜로……!"

    voice "audio/voice/v1_7_113.mp3"  
    f "에이지는 바닥에서 낮잠을 자고 있는 채인 루가몬을 봤다."

    voice "audio/voice/v1_7_114.mp3"  
    ryusenji "자네에게 일을 맡긴 내 눈이 옹이구멍이 아니어서 다행이야"

    voice "audio/voice/v1_7_115.mp3"  
    e "그렇단 건, 전 이녀석…… 루가몬을, 지금 당장 진화시킬 수 있다거나 하는 건가요?! 성숙기…… 완전체, 궁극체로!"

    voice "audio/voice/v1_7_116.mp3"  
    ryusenji "그건 알 수 없어"

    voice "audio/voice/v1_7_117.mp3"  
    e "어째서요?"

    voice "audio/voice/v1_7_118.mp3" 
    ryusenji "DS치는, 어디까지나 퍼텐셜을 가리키는 지표야" 

    voice "audio/voice/v1_7_119.mp3"  
    e "즉 가능성은 있는 거구나……!"

    voice "audio/voice/v1_7_120.mp3" 
    f "에이지는 완전히 의욕이 가득 채워졌다."

    voice "audio/voice/v1_7_121.mp3"  
    f "디지몬과의 상성……."

    voice "audio/voice/v1_7_122.mp3"  
    f "에이지는 그런 걸 그다지 생각해본 적은 없었다."

    voice "audio/voice/v1_7_123.mp3" 
    f "물론 디지몬이 툴로서 자신이 쓰기 쉬운지 아닌지는 있었지만." 

    voice "audio/voice/v1_7_124.mp3"  
    e "저는…… 티라노몬이라던가, 어느 정도, 다들 쓰고 있는 디지몬밖에 접해본 적이 없었어요"

    voice "audio/voice/v1_7_125.mp3"  
    f "크래커 사이에서 디지몬이 보급되어 있는 만큼 툴의 조정이 쉽다."

    voice "audio/voice/v1_7_126.mp3"  
    f "듣고 베끼면 되니까다."

    voice "audio/voice/v1_7_127.mp3"  
    f "최근 들어서는 사이보그형이 유행하고 있다는 듯하지만."

    voice "audio/voice/v1_7_128.mp3"  
    ryusenji "지금까지 디지몬은 어디서 입수해 왔던 건가? GriMM인가"

    voice "audio/voice/v1_7_129.mp3"  
    e "네. 일본에서는 반쯤 비합법이지만요"

    voice "audio/voice/v1_7_130.mp3"
    ryusenji "합법인 나라도 있으니까 말이지. 네트워크…… 디지털 월드에는 국경도 법률도 없다"  

    voice "audio/voice/v1_7_131.mp3" 
    e "그거! 「디지털 월드에 국경은 없다.」"

    voice "audio/voice/v1_7_132.mp3"  
    ryusenji "에이지 군…… 자네는, 그것이 누구의 말인지 알고 있는가"

    voice "audio/voice/v1_7_133.mp3"  
    f "류센지가 물었다."

    voice "audio/voice/v1_7_134.mp3"  
    e "…………"

    voice "audio/voice/v1_7_135.mp3"  
    f "에이지는 말문이 막혔다."

    voice "audio/voice/v1_7_136.mp3" 
    e "누구랄까…… 모두가?" 

    voice "audio/voice/v1_7_137.mp3"  
    e "GriMM의 크래커가 입에 달고 다니는 말이죠. 유래 같은 게 있나요?"

    voice "audio/voice/v1_7_138.mp3" 
    f "그 대답에, 류센지는 배우처럼 어깨를 으쓱였다."

    voice "audio/voice/v1_7_139.mp3"  
    ryusenji "에이지 군, 자네의 직업은?"

    voice "audio/voice/v1_7_140.mp3"
    e "크래커요"  

    voice "audio/voice/v1_7_141.mp3"  
    ryusenji "그럼「크랙팀」을 알고 있겠지"

    "Chapter 1-7 End..." with Pause(20)
# 챕터 1-8 시작
label Chapter1_8:

    scene black with blinds
    scene bg_chap_1_8 with blinds
 
    voice "audio/voice/v1.mp3"
    "Chapter1-8" "Eiji: Wolf of ninth avenue" 

    scene bg_chap_1_8_1 with fade

    voice "audio/voice/v1_8_1.mp3"
    f "――「크랙팀」"

    voice "audio/voice/v1_8_2.mp3"
    f "네트워크의 자유, 디지털 월드의 자유를 목적으로 하여"

    voice "audio/voice/v1_8_3.mp3"
    f "그 공통 이념의 아래 찬동하는 익명의 개인들로 구성된 커뮤니티다."

    voice "audio/voice/v1_8_4.mp3"
    f "회원 명부가 있는 것도 아니다."

    voice "audio/voice/v1_8_5.mp3"
    f "사이좋은 동호회 클럽도 아니다."

    voice "audio/voice/v1_8_6.mp3"
    f "크랙팀 내에서도 다양한 그룹이 있다."

    voice "audio/voice/v1_8_7.mp3"
    f "사상도, 행동원리도 목적도 다르다. "

    voice "audio/voice/v1_8_8.mp3"
    f "종종 팀 내에서도 다투기도 한다."

    voice "audio/voice/v1_8_9.mp3"
    f "크랙팀은 기존의 법과 권력―― 정부와는 반목하고 있다."

    voice "audio/voice/v1_8_10.mp3"
    f "반 사회적 집단이라는 꼬리표를 단, 부적합자 집단."

    voice "audio/voice/v1_8_11.mp3"
    f "그것이 소거법에 따른 공통점이었다."

    voice "audio/voice/v1_8_12.mp3"
    f "그럼에도 크래커라 자칭하는 자는 많든 적든 크랙팀의 이념에 찬동하여, 느긋하게 그 활동에 참가하고 있는 것이다."

    scene bg_chap_1_2_4 with fade
    show hacktv at Position(xalign = 0.5,yalign = 0.3) with squares

    voice "audio/voice/v1_8_13.mp3"
    f "모니터에 GriMM의 영상 서비스에 업로드된 크랙팀 선전용 숏 무비가 재생되었다."

    voice "audio/voice/v1_8_14.mp3"
    ryusenji nomal "――네트워크의 자유, 디지털 월드의 자유…… 디지털 월드에는 국경도 법률도 없다."

    voice "audio/voice/v1_8_15.mp3"
    ryusenji "그래서 디지몬을 사용한 모든 활동을 어떤 정부, 법률로도 막을 수는 없다"

    voice "audio/voice/v1_8_16.mp3"
    f "류센지가 말한다."

    voice "audio/voice/v1_8_17.mp3"
    f "그것이 크래커 측이 자주 말하는 변명이다."

    voice "audio/voice/v1_8_18.mp3"
    e nomal "어려운 걸 잘 모르겠지만. 연줄도 학력도 아무것도 없는 제게는 가장 벌어먹고 살 수 있는 일이었으니까요"

    voice "audio/voice/v1_8_19.mp3"
    f "크래커에 흥미를 갖게 된 것은 고등학교 재학 중이었다."

    voice "audio/voice/v1_8_20.mp3"
    f "살짝 나쁜 선배에게 꼬드겨져 크래커 놀이로 용돈 벌이를 하는 걸 배웠다…… 자주 있는 이야기다."

    voice "audio/voice/v1_8_21.mp3"
    f "적성에 맞는 걸지도 모른다. 아르바이트로서는 충분히 돈이 됐다."

    voice "audio/voice/v1_8_22.mp3"
    f "그것이 여러 사정이 있어서 대학 수험을 포기하고 나서 에이지는 진심으로 크래커를 목표로 삼게 되었다."

    voice "audio/voice/v1_8_23.mp3"
    f "이걸로 인생을 먹고 살아볼까, 라고."

    voice "audio/voice/v1_8_24.mp3"
    ryusenji "원하는 대로 할 수 있어서 좋겠군"

    voice "audio/voice/v1_8_25.mp3"
    e "정말 그래요! 원하는 대로 일할 수 있는 것 뿐이지만요"

    voice "audio/voice/v1_8_26.mp3"
    ryusenji "하지만 정부에게 있어서 크래커는 민폐만 끼치는 네트워크의 불량배일세"

    voice "audio/voice/v1_8_27.mp3"
    e "함정에는 신경 쓰고 있어요! 욕심 부리면 「디지대」가 오니까 말이죠"

    voice "audio/voice/v1_8_28.mp3"
    f "경찰의 사이버 범죄를 다루는 부서에는 디지몬 범죄에 대응하는 팀이 있다."

    scene black with fade
    show dd at Position(yalign = 0.4) with dissolve

    voice "audio/voice/v1_8_29.mp3"
    f "통칭 디지대."

    voice "audio/voice/v1_8_30.mp3"
    f "공개적으로 드러나지 않은 뒤쪽 조직이지만, 크래커 사이에서는 알려져 있었다."

    voice "audio/voice/v1_8_31.mp3"
    f "아주 최근에도 디지타마를 밀렵하고 있던 크래커 놀이를 하던 고등학생이 디지대에 검거되었다는 것 같지만."

    scene bg_chap_1_2_4 with fade
    show hacktv at Position(xalign = 0.5,yalign = 0.3) with squares

    voice "audio/voice/v1_8_32.mp3"
    ryusenji nomal "크랙팀에는 참가하고 있지만 이념에는 그다지 흥미가 없다."

    voice "audio/voice/v1_8_33.mp3"
    ryusenji "자네에게 있어서 자유란, 그건가, 패션 감각인가"

    voice "audio/voice/v1_8_34.mp3"
    e nomal "얕아 빠졌지요~! 그래도, 지금은 일거리와 실적을 원하거든요!"

    voice "audio/voice/v1_8_35.mp3"
    ryusenji "실적인가…… 자네의 미래는, 어디로 이어져 있는 걸려나. 에이지 군, 자네…… 그래, 꿈은"

    voice "audio/voice/v1_8_36.mp3"
    e "저…… 이기고 싶어요!"

    voice "audio/voice/v1_8_37.mp3"
    f "에이지는 솔직한 기분을 대답했다."

    voice "audio/voice/v1_8_38.mp3"
    ryusenji "호오, 무엇에 이기고 싶지?"

    voice "audio/voice/v1_8_39.mp3"
    e "현실에서는 어렵지만 넷에서라면…… 그렇다기보다 넷에서 거물이 되어, 올라가면 현실도 바뀔 테니까!" 

    voice "audio/voice/v1_8_40.mp3"
    e "그러기 위해서 벌어서, 디지몬을 진화시켜서…… 초일류 크래커가 되고 싶어! 그야말로 내 팀을 가질 수 있을 정도의!"

    voice "audio/voice/v1_8_41.mp3"
    ryusenji "그것은 크래커가 아니면 이룰 수 없는 건가?"

    voice "audio/voice/v1_8_42.mp3"
    e "응! 제게 있어서 디지털 월드는…… 분명, 제 인생을 바꿔줄 장소니까……!"

    voice "audio/voice/v1_8_43.mp3"
    f "예감이 있다."

    voice "audio/voice/v1_8_44.mp3"
    f "이 일은 에이지가 초일류 크래커가 될, 인생을 바꿀 천재일우의 찬스다."

    voice "audio/voice/v1_8_45.mp3"
    e "――저도 류센지 교수님과 같은 레벨이 되고 싶어요!"

    voice "audio/voice/v1_8_46.mp3"
    e "모니터나 관측 데이터가 아닌, 인간의 오감으로 직접 디지털 월드를 파악하는…… 그런 게 가능하다면, 할 수 있다면……!"

    voice "audio/voice/v1_8_47.mp3"
    f "있는 그대로."

    voice "audio/voice/v1_8_48.mp3"
    f "――디지털 월드에서, 만약 살아갈 수 있다면."

    voice "audio/voice/v1_8_49.mp3"
    f "에이지의 그 말을 들었을 때, 류센지는 확실히 웃은 것이었다."

    hide hacktv with dissolve
    show ryusenji at Position(xalign = 0.5,yalign = -0.2) with dissolve

    voice "audio/voice/v1_8_50.mp3"
    ryusenji "디지털 월드는 말이지…… 사람의 인생을 바꾼다네"

    voice "audio/voice/v1_8_51.mp3"
    f "나처럼 말이지, 라고."

    voice "audio/voice/v1_8_52.mp3"
    f "에이지는, 그것을 세계에서도 손에 꼽을 자산가가 된, 성공한 사람의 말로서 받아들였다."

    voice "audio/voice/v1_8_53.mp3"
    f "자신에게는 지금, 아무것도 없다."

    voice "audio/voice/v1_8_54.mp3"
    f "재산도 학력도, 덤으로 여친도."

    voice "audio/voice/v1_8_55.mp3"
    f "그럴 마음의 여유가 없었다. 다다미 3장 넓이의 무척 좁은 원룸, 건강에 나쁘고 불규칙한 식생활."

    voice "audio/voice/v1_8_56.mp3"
    f "살아가기만 할 뿐이라면 젊은 동안에는 되겠지만."

    voice "audio/voice/v1_8_57.mp3"
    f "그래서는 그저 늙으면서 시간을 소비할 뿐인 것이다."

    voice "audio/voice/v1_8_58.mp3"
    f "그래서는 재미없다."

    voice "audio/voice/v1_8_59.mp3"
    e "나는…… 지금의 인생을 바꾸고 싶어! 디지털 월드에서 이기고 싶어!"

    voice "audio/voice/v1_8_60.mp3"
    f "――각오."

    voice "audio/voice/v1_8_61.mp3"
    f "그래서, 모처럼 찾아온 류센지와의 연줄을 절대로 놓을 생각은 없었다."

    voice "audio/voice/v1_8_62.mp3"
    f "아무리 힘든 일이 있더라도, 이 육성 일도 디지몬 링커도, 루가몬도…… 눈에 흙이 들어가더라도 자기 것으로 삼고 싶다."

    voice "audio/voice/v1_8_63.mp3"
    f "무슨 일이 있더라도, 다."

    voice "audio/voice/v1_8_64.mp3"
    ryusenji "계속 봐 왔을 터인, 알고 있었을 터인 세계를, 보는 측면을 바꾸는 것으로 처음으로 이해할 수 있는 일도 있지"

    voice "audio/voice/v1_8_65.mp3"
    f "류센지가 중얼거렸다."

    voice "audio/voice/v1_8_66.mp3"
    e "…………?"

    voice "audio/voice/v1_8_67.mp3"
    ryusenji "잘 됐군. 실로 좋아. 루가몬을 육성해주었으면 한다고는 했지만, 그건 동시에 에이지 군, 자네를 테스트하고 있었던 걸세"

    voice "audio/voice/v1_8_68.mp3"
    e "아-…… 또 그런 소리 하신다니까!"

    voice "audio/voice/v1_8_69.mp3"
    ryusenji "사상까지 크랙팀에 푹 빠져있었더라면. "

    voice "audio/voice/v1_8_70.mp3"
    ryusenji "자유에 취해서, 자유를 낭비하고 있는 행복하고 어리석은 젊은이었다면 이 일을 부탁할 생각은 없었어"

    scene black with fade
    show soc at Position(yalign = 0.4) with dissolve

    voice "audio/voice/v1_8_71.mp3"
    f "――「SoC」"

    voice "audio/voice/v1_8_72.mp3"
    f "3글자의 알파벳을 모은 문장(徽章)―― 배지."

    voice "audio/voice/v1_8_73.mp3"
    f "선전 무비에 등장한 이 마크는, 넷의 언더그라운드를 들여다본 자라면 본 적이 있을 터이다."

    hide soc with dissolve
    scene bg_chap_1_2_4 with fade
    show ryusenji at Position(xalign = 0.5,yalign = -0.2) with dissolve

    voice "audio/voice/v1_8_74.mp3"
    e nomal "선즈 오브 케이오스……！"

    voice "audio/voice/v1_8_75.mp3"
    f "에이지는 숨을 삼켰다."

    voice "audio/voice/v1_8_76.mp3"
    ryusenji "혼돈의 아들들, 이라고 하면 되려나. 알고 있겠지"

    voice "audio/voice/v1_8_77.mp3"
    e "물론이죠! 초 유명한 크래커 집단……"

    voice "audio/voice/v1_8_78.mp3"
    ryusenji "자네의 SoC에 대한 솔직한 인상은?"

    voice "audio/voice/v1_8_79.mp3"
    e "…………"

    voice "audio/voice/v1_8_80.mp3"
    f "에이지는 대답했다." 

    voice "audio/voice/v1_8_81.mp3"
    e "위험한 놈들, 이려나요"

    voice "audio/voice/v1_8_82.mp3"
    f "그들은 초일류다. 동경하는 마음은 있다."

    voice "audio/voice/v1_8_83.mp3"
    f "하지만, 무사태평하고 요령 있게 인생을 즐기고 싶다면 관련되어서는 안 되는 무리다."

    voice "audio/voice/v1_8_84.mp3"
    f "과격파."

    voice "audio/voice/v1_8_85.mp3"
    f "크랙팀에서도 최고 우익이라고 하는 무투파 조직."

    voice "audio/voice/v1_8_86.mp3"
    e "――디지몬을 사용한 범죄…… 정보 절도, 기업 협박, 사이버 테러, 뭐든 다 있지."

    voice "audio/voice/v1_8_87.mp3"
    e "하지만 SoC의 리더는 카리스마가 있다! 그 『키클롭스(외눈 거인) 사건』의 주도자, 세계와 맞대결한 전설의 크래커 「타르타로스」……!"

    voice "audio/voice/v1_8_88.mp3"
    f "키클롭스 사건에 대해 여기서 언급하지는 않는다."

    voice "audio/voice/v1_8_89.mp3"
    f "크래커 그리고 크랙팀이라는 존재, 디지털 월드의 존재를, 국제 사회의 수뇌들이 무시할 수 없게 된, 커다란 계기가 된 일이었다."

    voice "audio/voice/v1_8_90.mp3"
    f "SoC의 리더, 크래커 타르타로스는 정체불명."

    voice "audio/voice/v1_8_91.mp3"
    f "일본인이라는 것 같다는 것 이외에는 소문다운 소문도 없다."

    voice "audio/voice/v1_8_92.mp3"
    ryusenji "다크 히어로라고 하는 건가. 타르타로스는 인기인이다. 나 같은 것보다도, 훨씬 더"

    voice "audio/voice/v1_8_93.mp3"
    f "류센지는 웃었다."

    voice "audio/voice/v1_8_94.mp3"
    e "GriMM에도 타르타로스의 신자는 많지만…… 그런 과격파가 지나치게 눈에 띄면 법 규제가 엄격해진다고 싫어하는 녀석도 똑같이 있어요"

    voice "audio/voice/v1_8_95.mp3"
    ryusenji "그 점일세"

    voice "audio/voice/v1_8_96.mp3"
    f "류센지는 에이지를 봤다."

    voice "audio/voice/v1_8_97.mp3"
    ryusenji "그들 SoC는 너무나도…… 나쁜 의미로 디지털 월드에 간섭하고 있어."

    voice "audio/voice/v1_8_98.mp3"
    ryusenji "과한 간섭에 의해 디지몬의 생태계, 나아가서는 인간 사회의 리스크를 낳고 있지."

    voice "audio/voice/v1_8_99.mp3"
    ryusenji "당연히 내 연구에도. 나는, 그렇게 되는 것을 지극히 우려하고 있네"

    voice "audio/voice/v1_8_100.mp3"
    e "...네"

    voice "audio/voice/v1_8_101.mp3"
    ryusenji "디지털 월드와 리얼월드…… 법적 규제의 강화에 의해 두 세계가 지금 이상으로 격리되어 버리는 일은, 인류에게 있어서도 디지몬에게 있어서도 불행한 일이다. "
    
    voice "audio/voice/v1_8_102.mp3"
    ryusenji "그렇게 생각하지는 않는가?"

    voice "audio/voice/v1_8_103.mp3"
    f "류센지는, 크래커에 대해서는 중립적인 입장을 취하고 있었다."

    voice "audio/voice/v1_8_104.mp3"
    f "그렇지 않다면 에이지에게 일을 의뢰하거나 하지는 않았을 것이다."

    voice "audio/voice/v1_8_105.mp3"
    f "하지만, 디지몬을 사용한 흉악 범죄, 테러리스트에 대해서는 깊게 우려하고 있다."

    voice "audio/voice/v1_8_106.mp3"
    f "그것은, 단적으로 말해서 디지몬을 사랑하고 있기 때문이다."

    voice "audio/voice/v1_8_107.mp3"
    f "류센지가 용서하지 못하는 것은, 디지몬을 악용해서 위험에 빠뜨리는 인간이며 크래커였다."

    voice "audio/voice/v1_8_108.mp3"
    e "교수님이라면 정부라던가 정치가에게도 인맥이 통하는 거 아닌가요……?"

    voice "audio/voice/v1_8_109.mp3"
    f "에이지는 되물었다."

    voice "audio/voice/v1_8_110.mp3"
    f "류센지는 테크놀로지 연관 정부 유식자, 디지털 월드 특별 고문이다."

    voice "audio/voice/v1_8_111.mp3"
    f "분명 경찰의 장비품 선정에도 관련되어 있었을 터이다."

    voice "audio/voice/v1_8_112.mp3"
    ryusenji "물론 로비는 해 왔지. 그렇지만, 지금 총리는 검토만 하고 실행력이 없어서 말일세……"

    voice "audio/voice/v1_8_113.mp3"
    ryusenji "경찰로 말하자면 법률에 따라 크래커를 단속할 뿐이야."

    voice "audio/voice/v1_8_114.mp3"
    ryusenji "관련법은 미정비, 불충분해서…… 좀처럼 잘 풀리지 않아"

    voice "audio/voice/v1_8_115.mp3"
    e "교수님…… 왠지 이야기가, 위험한 쪽으로 향하고 있는 것 같은데요"

    voice "audio/voice/v1_8_116.mp3"
    ryusenji "그만 듣겠는가"

    voice "audio/voice/v1_8_117.mp3"
    e "설마요……! 두근거리기 시작했어요!"

    voice "audio/voice/v1_8_118.mp3"
    f "크래커로서 해 나가겠다고 결정했을 때부터, 언젠가는―― 이런 일을 하고 싶다고 생각해 왔다."

    voice "audio/voice/v1_8_119.mp3"
    f "디지몬의 포획이나 디지타마 채취, 정크 데이터 수집이 아니라."

    voice "audio/voice/v1_8_120.mp3"
    f "크래커로서, 다른 크래커를 상대하는…… 그런 위험한 향기가 감도는 어른의 일을."

    voice "audio/voice/v1_8_121.mp3"
    ryusenji "잠입 조사다, 선즈 오브 케이오스에."

    voice "audio/voice/v1_8_122.mp3"
    ryusenji "수수께끼의 리더 타르타로스의 목적에 다가가주었으면 한다."

    voice "audio/voice/v1_8_123.mp3"
    ryusenji "모든 것은 디지털 월드와 디지몬을 위해서다, 그들을 지키기 위해서……!"
    
    "Chapter 1-8 End..." with Pause(20)
# 챕터 1-9 시작
label Chapter1_9:

    scene black with blinds
    scene bg_chap_1_9 with blinds
 
    voice "audio/voice/v1.mp3"
    "Chapter1-9" "Eiji: Wolf of ninth avenue" 

    voice "audio/voice/v1_9_1.mp3"
    f "에이지는 류센지 교수에게, 무투파 크래커 집단 선즈 오브 케이오스(SoC)의 조사를 의뢰받았다."

    voice "audio/voice/v1_9_2.mp3"
    f "――한 크래커로서 SoC에 참가. 리더 타르타로스와 접촉을 꾀하여, 그 목적을 파헤쳐 주었으면 한다."

    voice "audio/voice/v1_9_3.mp3"
    f "크랙팀에서도 최악 최강이라고 일컬어지는 무투파 조직 SoC."

    voice "audio/voice/v1_9_4.mp3"
    f "그것이 최근, 대규모 「활동」을 계획하고 있다는 징후가 있다고 한다."

    voice "audio/voice/v1_9_5.mp3"
    f "전 세계의 첩보기관, 경찰이 움직이고 있지만, 류센지로서도 디지털 월드에 관한 것은 전혀 남 일은 아니었다. "

    voice "audio/voice/v1_9_6.mp3"
    f "그래서 독자적으로 크래커를 고용하여 조사를 하는 것이다."

    voice "audio/voice/v1_9_7.mp3"
    f "――디지털 월드와 디지몬을 지키기 위해."

    voice "audio/voice/v1_9_8.mp3"
    f "보수는 파격적. 하지만, 무엇보다도 에이지의 마음을 움직였던 것은 류센지의, 그 마음이었다."

    voice "audio/voice/v1_9_9.mp3"
    f "SoC와 타르타로스의 활동에 의해, 국제사회가 크래커뿐 아니라 디지털 월드를 위험시하여, 디지몬을 적시하게 된다면……."

    voice "audio/voice/v1_9_10.mp3"
    f "――디지털 월드의 생태계, 즉 디지몬의 생명에 관련된 일이 된다."

    voice "audio/voice/v1_9_11.mp3"
    f "한때 유럽이나 미국, 일본에서도, 가축을 덮친다는 이유만으로 늑대는 절멸당했다."

    voice "audio/voice/v1_9_12.mp3"
    f "그런 비극을 디지털 월드에서 재현되는 일은 피해야만 한다."

    voice "audio/voice/v1_9_13.mp3"
    f "디지몬은 살아 있다."

    voice "audio/voice/v1_9_14.mp3"
    f "존경하는 류센지의 생각을 듣고, 에이지는 강하게 영향을 받았다."

    voice "audio/voice/v1_9_15.mp3"
    e "즉, 나는 스파이라는 거지"

    voice "audio/voice/v1_9_16.mp3"
    f "에이지는 말을 걸었다."

    scene bg_chap_1_6_2 with fade # 추후 이미지 변경 필요

    voice "audio/voice/v1_9_17.mp3"
    f "자택인 무척이나 좁은 원룸."

    voice "audio/voice/v1_9_18.mp3"
    f "2층 침대의 이불 발치에, 복슬복슬한 무언가가 배를 내보이며 벌렁 드러누워 있다."

    voice "audio/voice/v1_9_19.mp3"
    f "루가몬, 의 홀로라이즈다."

    voice "audio/voice/v1_9_20.mp3"
    f "임대 주거라 애완동물은 금지지만, 디지털 펫은 꼭 그렇지만도 않다."

    voice "audio/voice/v1_9_21.mp3"
    e "알겠냐 루가몬! 우리는 SoC에 잠입한다. 전설의 크래커 타르타로스의 정체에 다가서는 거야. 얕보이지 말라고"

    voice "audio/voice/v1_9_22.mp3"
    f "말을 건다."

    voice "audio/voice/v1_9_23.mp3"
    f "디지몬에게 말을 걸다니, 지금까지 해 본 적은 없었다."

    voice "audio/voice/v1_9_24.mp3"
    f "루가몬이 드러누운 채로 이누코로(犬コロ)처럼 목을 갸웃거렸다."

    voice "audio/voice/v1_9_25.mp3"
    f "디지몬이 사람의 말을 어디까지 이해하는지에 관해서는 다양한 견해가 있지만……."

    voice "audio/voice/v1_9_26.mp3"
    e "뭐라고 해도 상대는 SoC! 크래커 중에서도 확고한 초 무서운 형씨들이다."

    voice "audio/voice/v1_9_27.mp3"
    e "평범한 티라노몬으로는 얕보이고 말 거야. 그런가 하면 너는, 성장기라고는 해도 레어한 느낌은 풀풀 나니까"

    voice "audio/voice/v1_9_28.mp3"
    f "에이지의 ――크래커 팽의 이름을 선전한다. 우선은, 거기서부터다."

    voice "audio/voice/v1_9_29.mp3"
    f "손을 뻗는다."

    voice "audio/voice/v1_9_30.mp3"
    f "루가몬의 이마에 있는, 그 파츠 부분을 쓰다듬는다."

    voice "audio/voice/v1_9_31.mp3"
    f "물론 실제로는 만질 수 없지만…… "

    voice "audio/voice/v1_9_32.mp3"
    f "갑자기 루가몬은 으르렁거리며 이를 내보였다."

    voice "audio/voice/v1_9_33.mp3"
    e "아-, 싫은 거구나. 미안미안…… 그러고보니 옛날에 길렀던 개도 쓰다듬으려고 하면 기분 나빠했었던가"

    voice "audio/voice/v1_9_34.mp3"
    f "부모님은 잘 따랐었지만, 어째선지 에이지에게만은 그런 태도를 취했던 개였다."

    voice "audio/voice/v1_9_35.mp3"
    "삐 삐 삐 삐"

    voice "audio/voice/v1_9_36.mp3"
    f "약속의, 일 시간이다."

    voice "audio/voice/v1_9_37.mp3"
    e "갈까, 루가몬"

    voice "audio/voice/v1_9_38.mp3"
    f "홀로라이즈를 해제. 루가몬은 디지몬 링커의 화면 속으로 돌아간다."

    voice "audio/voice/v1_9_39.mp3"
    f "보이스 채팅용 인컴을 귀에 꽂고, 에이지는 2층침대의 벽에 기대어 디지몬 링커의 메뉴를 열었다."

    scene bg_chap_1_9_1 with fade

    voice "audio/voice/v1_9_40.mp3"
    "슈우우웅"

    voice "audio/voice/v1_9_41.mp3"
    f "헤드업으로 가상 모니터가 투영된다. 이것도 홀로라이즈 기술의 응용이다."

    voice "audio/voice/v1_9_42.mp3"
    f "ㅡㅡ 가상 모니터에 네트워크를 연결하고, GriMM으로 이동."

    voice "audio/voice/v1_9_43.mp3"
    f "SoC에 참가하는 것 자체는, 아무것도 어려울 것은 없다."

    voice "audio/voice/v1_9_44.mp3"
    f "GriMM의 멤버 모집에서 초대 코드를 손에 넣으면 아르바이트 모집 감각으로 SoC의 전용 채널에 참가가 가능하다."

    voice "audio/voice/v1_9_45.mp3"
    f "에이지는 미리 SoC에 응모하여, 약속을 잡아 두었던 것이었다."

    voice "audio/voice/v1_9_46.mp3"
    "면접관" "――SoC가 상대하는 것은, 정부 기관, 군, 경찰, 세계적 기업…… 그런 무리들입니다."

    voice "audio/voice/v1_9_47.mp3"
    "면접관" "요구되어지는 크래커 스킬은, 딱 잘라 말해 높지요. 더욱이 리스크밖에 없습니다"

    voice "audio/voice/v1_9_48.mp3"
    f "SoC의 선배 멤버가, 보이스 채팅으로 에이지의 상대를 해 주었다."

    voice "audio/voice/v1_9_49.mp3"
    f "온라인 면접이다."

    voice "audio/voice/v1_9_50.mp3"
    e nomal "참가 희망은 간단하지만, 크래커로서의 스킬이 없으면 문전박대인가"

    voice "audio/voice/v1_9_51.mp3"
    "면접관" "당신은 어떤가요, 신인 씨"

    voice "audio/voice/v1_9_52.mp3"
    e "「팽이야」"

    voice "audio/voice/v1_9_53.mp3"
    "면접관" "네, 크래커 팽. 당신의, 지금 리얼에서의 생활을 천칭에 걸고서라도, SoC의 활동에 참가하고 싶습니까"

    voice "audio/voice/v1_9_54.mp3"
    f "상대의 유저 네임은 「면접관」이라고만 되어 있다."

    voice "audio/voice/v1_9_55.mp3"
    f "GriMM에서의 아이콘은 넥타이를 머리띠처럼 맨 정석적인 쇼와 샐러리맨풍. 왠지 모르게…… 계장? 목소리는, 꽤나 든 아저씨 같지만."

    voice "audio/voice/v1_9_56.mp3"
    e "저기…… 반대로, 스킬을 인정받으면 「타르타로스」를 만날 수 있거나 한 거야?"

    voice "audio/voice/v1_9_57.mp3"
    f "에이지는 점점 파고들었다."

    voice "audio/voice/v1_9_58.mp3"
    f "크래커끼리는, 네트워크상에서는 기본적으로 반말 OK, 털털한 말투가 된다."

    voice "audio/voice/v1_9_59.mp3"
    "면접관" "리더에게 흥미가?"

    voice "audio/voice/v1_9_60.mp3"
    f "면접관의 목소리에, 얼마간 경계의 색이 섞였다."

    voice "audio/voice/v1_9_61.mp3"
    e "그야 물론! 전설급의 천재 크래커잖아!"

    voice "audio/voice/v1_9_62.mp3"
    "면접관" "하하핫…… 당신, 엄청 어리군요. 고등학교…… 아니 중학생?"

    voice "audio/voice/v1_9_63.mp3"
    f "면접관은 웃었다."

    voice "audio/voice/v1_9_64.mp3"
    e "그러는 면접관 씨는 몇 살인가요?"

    voice "audio/voice/v1_9_65.mp3"
    "면접관" "환갑의 영감이라고 대답해도 17살 여고생이라고 대답해도, 그런 건 어떻게 증명하지요?"

    voice "audio/voice/v1_9_66.mp3"
    "면접관" "여기서는 각자가 믿는 식으로밖에 보이지 않고 들리지 않아요"

    voice "audio/voice/v1_9_67.mp3"
    e "굳이 자신의 네트워크 이용 능력이 높은 걸 주장하는 건, 어떤 특정한, 괴로운 세대의 아저씨의 특징이죠"

    voice "audio/voice/v1_9_68.mp3"
    f "에이지는 직감했다. 아마 면접관은 리얼에서도 아저씨다."

    voice "audio/voice/v1_9_69.mp3"
    "면접관" "…………"

    voice "audio/voice/v1_9_70.mp3"
    e "아, 계속 말씀해주세요"

    voice "audio/voice/v1_9_71.mp3"
    f "약간의 공백이 있었다."

    voice "audio/voice/v1_9_72.mp3"
    "면접관" "…………리더 타르타로스는 수수께끼입니다. 저 같은 말단 멤버는 목소리조차 들어본 적 없지요"

    voice "audio/voice/v1_9_73.mp3"
    e "수수께끼"

    voice "audio/voice/v1_9_74.mp3"
    f "그런 설정인가."

    voice "audio/voice/v1_9_75.mp3"
    "면접관" "당신이 스스로 생각하고 있는 것 같은 천재 크래커이고, 실적을 올린다면, 가만히 있어도 간부 중 누군가가 접촉해 오겠죠."

    voice "audio/voice/v1_9_76.mp3"
    "면접관" "간부의 채팅에 참가할 수 있다면, 타르타로스와 이야기할 수 있을지도"

    voice "audio/voice/v1_9_77.mp3"
    f "꽤나 앞길이 먼 것 같다……."

    voice "audio/voice/v1_9_78.mp3"
    f "리더 타르타로스에게 접근할 방법은 알았다. 어쨌든 SoC의 활동에 참가하여 척척 실적을 쌓는다. 실력주의란 것이다."

    voice "audio/voice/v1_9_79.mp3"
    e "그래서, 지금부터 맡을 일이 SoC의 채용 시험이란 거야?"

    voice "audio/voice/v1_9_80.mp3"
    "면접관" "그렇게 생각해도 상관없습니다. 참고로 난이도는 준 Ａ급 상당…… 파일은 GriMM에 공유해 두겠습니다. 미션 전용 채널을 열어두지요"

    voice "audio/voice/v1_9_81.mp3"
    f "가상 모니터에 작전의 개요가 표시되었다."

    voice "audio/voice/v1_9_82.mp3"
    "면접관" "――작전명은…… 음, 뭐든지 상관없습니다만"

    voice "audio/voice/v1_9_83.mp3"
    e "「뒷문의 늑대」작전"

    voice "audio/voice/v1_9_84.mp3"
    f "에이지는 작전명을 리퀘스트했다."

    voice "audio/voice/v1_9_85.mp3"
    "면접관" "…………? 그건"

    voice "audio/voice/v1_9_86.mp3"
    e "아니, 막 떠오른 거"

    voice "audio/voice/v1_9_87.mp3"
    f "깊은 의미는 없다."

    voice "audio/voice/v1_9_88.mp3"
    f "굳이 말하자면 늑대―― 루가몬의 첫 출진이라는 것."

    voice "audio/voice/v1_9_89.mp3"
    f "에이지가 크래커로서 각오를 굳혔다는, 뒤로 물러날 수는 없다는…… 기합이다."

    voice "audio/voice/v1_9_90.mp3"
    "면접관" "a wolf at the back gate…… 알겠습니다. 기니까 『늑대 작전』으로"

    voice "audio/voice/v1_9_91.mp3"
    e "너무 잘랐잖아-"

    voice "audio/voice/v1_9_92.mp3"
    "면접관" "난이도 준 A급…… 정말로 괜찮겠습니까? 십중팔구 당신의 소중한 디지몬을 속수무책으로 잃게 될 겁니다. 말할 것도 없지만 보증, 보상은 없습니다"

    voice "audio/voice/v1_9_93.mp3"
    e "라져. 환영회를 준비해 두라고"

    voice "audio/voice/v1_9_94.mp3"
    "면접관" "환영? 무엇을 말이죠"

    voice "audio/voice/v1_9_95.mp3"
    e "새로운 SoC의 간부 탄생을 축하하는"

    voice "audio/voice/v1_9_96.mp3"
    f "호언장담."

    voice "audio/voice/v1_9_97.mp3"
    f "하지만 아무 대책도 없는 것은 아니다. 에이지에게는 비장의 수가 있는 것이다."

    scene black with fade

    show ryusenji at Position (xalign =0.5, yalign = -0.2) with dissolve
    voice "audio/voice/v1_9_98.mp3"
    ryusenji "――SoC에의 잠입에 대비하여 자네의 디지몬 링커의 기능을 한정 해제했네."

    scene bg_chap_1_9_1 with fade

    voice "audio/voice/v1_9_99.mp3"
    f "믿음직한 류센지는 이번 의뢰에 대비하여 크래커로서의 스킬을 한번에 올릴 수 있는 수단을 준비해 주었다."

    voice "audio/voice/v1_9_100.mp3"
    f "D4의 연구성과. 그야말로 「굴레」를 초월하기 위한――"

    voice "audio/voice/v1_9_101.mp3"
    e nomal "(봐 주겠어! 초일류가 보고 있는 세계를…… 할 수 있어! 이 디지몬 링커와, 류센지 교수님이 준 루가몬이 있으면!)"

    voice "audio/voice/v1_9_102.mp3"
    f "심호흡."

    voice "audio/voice/v1_9_103.mp3"
    "면접관" "작전의 내용은 파일을 확인해주세요. 그럼, 성공을 기원하겠습니다"

    voice "audio/voice/v1_9_104.mp3"
    e "고마워, 면접관 씨"

    voice "audio/voice/v1_9_105.mp3"
    f "에이지는 디지몬 링커의 화면을 바라보았다."

    # 추후 이미지 추가 필요
    #
    #

    voice "audio/voice/v1_9_106.mp3"
    f "작은 화면 속에서, 루가몬이 이쪽을 보고 있다."

    voice "audio/voice/v1_9_107.mp3"
    f "무언으로."

    voice "audio/voice/v1_9_108.mp3"
    e "(디지몬이 살아 있다…… 류센지 교수님이 말한 의미를, 분명, 알 수 있을 거야!)"

    voice "audio/voice/v1_9_109.mp3"
    f "메뉴를 선택."

    voice "audio/voice/v1_9_110.mp3"
    "삐비빅"

    voice "audio/voice/v1_9_111.mp3"
    f "센서가 생체 정보를 계측, 바이탈 체크 뒤에 커맨드를 허가했다."

    voice "audio/voice/v1_9_112.mp3"
    f "한정 해제."

    voice "audio/voice/v1_9_113.mp3"
    f "의식은 빛이 되어 해방될 것이다."

    voice "audio/voice/v1_9_114.mp3"
    f "자,"

    voice "audio/voice/v1_9_115.mp3"
    f "――「마인드 링크」!"

    scene black with flash
    voice "audio/voice/v1_9_116.mp3"
    "슈우우우웅"

    scene bg_chap_1_9_4 with fade
    "Chapter 1-9 End..." with Pause(20)

# label Chapter1_10:

#     scene black with blinds
#     scene bg_chap_1_10 with blinds
 
#     voice "audio/voice/v1.mp3"
#     "Chapter1-10" "Eiji: Wolf of ninth avenue" 
























    return