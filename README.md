# 🚀 Django & FastAPI 병행 학습 프로젝트

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-1D2951?style=flat-square&logo=starlette&logoColor=white)

이 프로젝트는 Python의 두 가지 주요 웹 프레임워크인 **Django**와 **FastAPI**를 단일 가상 환경에서 병행 학습하기 위해 구성되었습니다. **Django의 MVT 기반 웹 서비스** 구조와 **FastAPI의 고성능 REST API 서버** 구조를 비교 학습하는 것이 목표입니다.

| 프레임워크 | 역할 | 주요 학습 내용 |
| :--- | :--- | :--- |
| 🌐 **Django (blog\_project)** | MVT 기반 웹 서비스 | **MVT 패턴** 이해, DB 연동, 웹 페이지 목록 출력 |
| ⚡ **FastAPI** | 고성능 REST API 서버 | **Pydantic 모델** 사용, API 명세 자동화, 동적 라우팅 |

**1. 🌐 Django 블로그 프로젝트 (웹 서비스)
목표: Django의 MVT 아키텍처를 활용하여 웹 페이지 구축 학습.**

*주요 구현:*

모델: Post 모델 정의 및 DB 구조 설정.

데이터 관리: admin.py 등록을 통한 관리자 페이지에서 데이터 입력 및 확인.

목록 조회: /posts/ 경로 연결, views.py에서 DB 데이터를 가져와 post_list.html에 표시.

**2. ⚡ FastAPI API 서버 프로젝트
목표: 고성능 REST API 서버 구축 및 Pydantic 활용 학습.**

*주요 구현:*

기본 API: / 및 /api/v1/currencies 엔드포인트 정의.

Pydantic 모델: Currency 모델을 정의하여 데이터 구조 명세화. /docs의 Swagger UI 자동 생성.

*라우팅 확장:*

동적 경로 (Path Parameter): 특정 통화 코드(/api/v1/currencies/{code}) 조회 기능 추가.

쿼리 매개변수 (Query Parameter): ?min_rate={값}으로 최소 환율을 기준으로 목록 필터링 기능 추가.
