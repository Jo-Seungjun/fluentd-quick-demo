가장 빠르게 fluentd 를 써보기

fluentd 는 로그 수집기 이다.

로그를 수집하고 배포하는 과정을 fluentd 로 한번에 해결할 수 있다.

# fluentd 를 이해하는 과정
1. 로깅 시스템의 목적과 구조를 알아야 한다.
2. 각 파트의 역할을 알아야 한다.
3. 어디서 무엇을 담당해야하는지 구분할 수 있어야 한다.
4. 디버깅 할 수 있어야 한다
5. 문제를 디버깅 할 수 있어야 한다.
point 로깅 시스템의 흐름을 알아야 한다.

# 로깅 이란
로그는 직역하면 통나무 라는 뜻을 가지고 있다. 과거 선박을 항해할때 선박의 속도를 측정하기 위해 바다에 통나무(Log) 를 띄워 벌어지는 간격을 기반으로 속도를 측정했다고 한다 [(참조)](https://quod.lib.umich.edu/cgi/t/text/pageviewer-idx?cc=eebo2;c=eebo2;idno=a80170.0001.001;node=A80170.0001.001:15;seq=78;submit=Go;type=simple;vid=119140;q1=log;page=root;view=text). 따라서 현재의 상태를 알기위해 과거에 기록해두는 무언가 라는 의미가 상태를 확인하기 위해 시스템에서 발생한 이벤트들을 기록하는것 까지 확장되었다.

# 나에게 맞는 로깅 시스템 선정하기
로그는 그 종류와 용도가 다양한 만큼 구현하는 시스템도 다양하다. 필자가 핵심으로 생각하는 기준은 다음과 같다.
- 실시간 - 로그를 통해서 실시간으로 모니터링 할 필요가 있는 시스템
- 시계열 - 데이터의 종류가 시간의 흐름과 관계가 있는 시스템

# fluentd vs ELK

# fluentd 를 습득하는 과정
1. 로그가 발생되는 시스템을 지원하는 플러그인을 찾는다.
2. fluentd 를 설치 및 실행해본 뒤 fluent.conf 파일을 수정해 로그를 받아본다.
3. db 를 연결해 로그를 저장해본다.
4. 원하는대로 구현되지 않을 경우 이를 지원할 수 있는 방법을 찾아본다.
point fluentd.conf 를 수정하는 방법을 알아야 한다.