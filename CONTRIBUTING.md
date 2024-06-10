# Contributing Guidelines

Thank you for your interest in contributing to our Python project! We value your contributions and want to make sure the process is as easy as possible. This document outlines the guidelines and steps you need to follow to contribute effectively.

## 개발 환경 설정

시작하기 위해서는 로컬 개발 환경을 설정해야 합니다. 다음 단계를 따르세요:

1. **저장소 포크 및 클론:**
   - GitHub 계정에서 프로젝트를 포크합니다. "Fork" 버튼을 클릭하세요.
   - 포크한 저장소를 로컬 컴퓨터에 클론합니다:
     ```bash
     git clone https://github.com/Bulkrum/cliniquery.git
     cd cliniquery
     ```

2. **종속성 설치:**
   - 프로젝트마다 필요한 종속성을 따로 관리하기 위해 가상 환경을 사용하는 것이 좋습니다. `virtualenv`를 설치하지 않았다면 pip을 사용하여 설치하세요:
     ```bash
     pip install virtualenv
     virtualenv venv
     source venv/bin/activate  # Windows에서는 `venv\Scripts\activate`를 사용하세요
     ```
   - 프로젝트 종속성을 설치합니다:
     ```bash
     pip install -r requirements.txt
     ```

3. **pre-commit 훅 설치:**
   - 이 프로젝트는 커밋이 코딩 표준을 준수하는지 확인하기 위해 pre-commit 훅을 사용합니다. (`flake8`은 린팅에, `Black`은 코드 포맷팅에 사용)
   - pre-commit 훅을 설치합니다:
     ```bash
     pip install pre-commit
     pre-commit install
     ```

## 변경 사항 반영

1. **새 브랜치 생성:**
   - 변경 사항은 새로운 브랜치에서 작업해야 합니다:
     ```bash
     git checkout -b label/your-name
     ```

2. **변경하고 커밋하기:**
   - 로컬에서 논리적인 단위로 변경 사항을 만들고 git을 사용하여 커밋합니다:
     ```bash
     git add .
     git commit -m "문제 100개 라벨링 완료."
     ```

3. **pre-commit 체크 실행:**
   - 변경 사항을 푸시하기 전에 모든 pre-commit 체크를 통과했는지 확인하세요:
     ```bash
     pre-commit run --all-files
     ```
   - 훅에서 에러가 발생하면 수정하고 재실행하세요.

4. **변경 사항을 푸시하고 풀 리퀘스트 생성:**
   - 브랜치를 GitHub에 푸시합니다:
     ```bash
     git push origin label/your-name
     ```
   - GitHub에서 저장소로 이동하여 새로운 풀 리퀘스트를 생성합니다. pre-commit 체크를 통과했는지 확인하고, 기본 브랜치와 충돌이 없는지 확인하세요.

## 풀 리퀘스트 가이드라인

- 명확하고 설명적인 제목과 자세한 변경 사항 설명을 제공하세요.
- 관련된 이슈가 있다면 PR에 링크를 포함하세요.
- 기존 테스트가 깨지지 않도록 하고, 가능하다면 변경 사항을 커버하는 새로운 테스트를 추가하세요.
- 코딩 표준(PEP 8)을 따르고, 코드가 깔끔하고 잘 문서화되었는지 확인하세요.

## 코드 리뷰 프로세스

- 프로젝트 멤버를 포함한 모든 제출물은 리뷰가 필요합니다.
- 팀에서 제출물을 리뷰하고 수정 요청이나 피드백을 제공할 수 있습니다.
- 승인되면 팀 구성원이 PR을 병합합니다.

---

## Setting Up Your Development Environment

To get started, you'll need to set up your local development environment. Follow these steps:

1. **Fork and clone the repository:**
   - Fork the project to your GitHub account by clicking the "Fork" button.
   - Clone your fork to your local machine:
     ```bash
     git clone https://github.com/Bulkrum/cliniquery.git
     cd cliniquery
     ```

2. **Install dependencies:**
   - It's recommended to use a virtual environment to keep dependencies required by different projects separate. If you don’t have `virtualenv` installed, you can install it with pip:
     ```bash
     pip install virtualenv
     virtualenv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```
   - Install the project dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. **Install pre-commit hooks:**
   - This project uses pre-commit hooks to ensure that commits meet our coding standards (`flake8` for linting and `Black` for code formatting).
   - Install the pre-commit hooks:
     ```bash
     pip install pre-commit
     pre-commit install
     ```

## Making Changes

1. **Create a new branch:**
   - Changes should be made on a new branch:
     ```bash
     git checkout -b label/your-name
     ```

2. **Make and commit your changes:**
   - Make your changes locally and commit them in logical chunks using git:
     ```bash
     git add .
     git commit -m "Labeled 100 questions."
     ```

3. **Run pre-commit checks:**
   - Before pushing your changes, ensure that your changes pass all pre-commit checks:
     ```bash
     pre-commit run --all-files
     ```
   - If any hooks report errors, fix the errors and re-run the checks.

4. **Push your changes and create a pull request:**
   - Push your branch to GitHub:
     ```bash
     git push origin label/your-name
     ```
   - Go to the repository on GitHub and create a new pull but make sure it passes the pre-commit checks (these will run automatically on GitHub if set up) and does not conflict with the base branch.

## Pull Request Guidelines

- Provide a clear, descriptive title and a detailed description of your changes.
- Link to any relevant issues your PR addresses.
- Ensure your changes do not break the existing tests, and if possible, add new tests to cover your changes.
- Follow the coding standards (PEP 8) and ensure your code is clean and well-documented.

## Code Review Process

- All submissions, including submissions by project members, require a review.
- Our team will review your submission and possibly request changes or give feedback.
- Once approved, someone from the team will merge your PR.

Thank the contributor for their efforts, and remind them that their contributions are valued.
