<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<div align="center">
  <h1 align="center">Bộ Công Cụ Phát Triển iOS Theo Spec</h1>
  <p align="center">
    <a href="README.md">English</a> | Tiếng Việt
    <br />
    <br />
    Bộ workflow hướng sản xuất cho Claude Code và OpenCode.
    <br />
    Đi từ ý tưởng đến triển khai với bộ tài liệu rõ ràng: requirements -> design -> tasks -> code.
    <br />
    <br />
    <a href="https://github.com/nguyennamkkb/ios-spec-driven"><strong>Xem tài liệu »</strong></a>
    <br />
    <br />
    <a href="https://github.com/nguyennamkkb/ios-spec-driven/issues">Báo lỗi</a>
    ·
    <a href="https://github.com/nguyennamkkb/ios-spec-driven/issues">Đề xuất tính năng</a>
  </p>
</div>

<details>
  <summary>Mục lục</summary>
  <ol>
    <li><a href="#gioi-thieu">Giới thiệu</a></li>
    <li><a href="#vi-sao-hieu-qua">Vì sao hiệu quả</a></li>
    <li><a href="#cac-che-do-workflow">Các chế độ workflow</a></li>
    <li><a href="#bo-cong-cu-ban-nhan-duoc">Bộ công cụ bạn nhận được</a></li>
    <li><a href="#bat-dau-nhanh">Bắt đầu nhanh</a></li>
    <li><a href="#san-pham-dau-ra">Sản phẩm đầu ra</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#lien-he">Liên hệ</a></li>
  </ol>
</details>

## Giới thiệu

Nhiều phiên làm việc với AI bị giảm chất lượng ở bước handoff: yêu cầu chưa rõ, quyết định thiết kế rời rạc, và khó kiểm tra tính đúng đắn khi triển khai.

Bộ toolkit này đưa vào một mô hình thực thi có kỷ luật cho đội iOS:

- xác định outcome trước khi code
- chuyển outcome thành bộ spec có cấu trúc
- liên kết task triển khai với acceptance criteria
- thực thi theo chuẩn chung và checkpoint review

Toolkit hỗ trợ cả dự án mới lẫn phát triển tính năng trên codebase hiện có.

<p align="right">(<a href="#readme-top">lên đầu trang</a>)</p>

## Vì sao hiệu quả

- **Một luồng giao hàng thống nhất** từ ý tưởng tới triển khai, giảm chuyển ngữ cảnh
- **Spec có thể truy vết** giữa requirements, design và tasks
- **Chuẩn dùng lại được** cho architecture, UI components, testing và execution
- **Hỗ trợ 2 IDE** với chuyển đổi template tự động cho Claude Code và OpenCode
- **Workflow dựa trên agent** giúp tiến độ nhất quán giữa các thành viên

<p align="right">(<a href="#readme-top">lên đầu trang</a>)</p>

## Các chế độ workflow

### 1) Full Documentation Mode (dự án mới)

Dùng khi bắt đầu từ ý tưởng và cần bộ tài liệu mục tiêu có cơ sở thị trường trước khi triển khai.

`@write-project-docs` được dùng để:

- nghiên cứu bối cảnh thị trường, nhóm người dùng và các mẫu cạnh tranh
- làm rõ mục tiêu sản phẩm và tiêu chí thành công
- tạo bộ tài liệu mục tiêu đầy đủ để đồng bộ team trước khi code

```text
@write-project-docs Create complete documentation for [project name]
```

Ví dụ:

```text
@write-project-docs Create complete documentation for fitness tracking app
```

### 2) Feature Delivery Mode (dự án đang vận hành)

Dùng khi cần giao từng tính năng với traceability rõ ràng.

```text
Create spec for [feature name]
```

Ví dụ:

```text
Create spec for user login feature
```

Lối tắt cho thay đổi nhỏ:

```text
Quick implementation of [small feature]
```

Ví dụ:

```text
Update design: add caching layer for dashboard data
```

<p align="right">(<a href="#readme-top">lên đầu trang</a>)</p>

## Bộ công cụ bạn nhận được

### 7 Specialized Skills

| Skill | Mục đích |
|---|---|
| `dev-spec-driven` | Điều phối workflow và kỷ luật quy trình |
| `ios-architecture` | MVVM, Clean Architecture, SwiftUI patterns |
| `ios-components` | Chuẩn component UI tái sử dụng |
| `ios-ui-ux` | UX patterns và accessibility |
| `ios-debug` | Debugging và tối ưu hiệu năng |
| `mcp-xcode` | Build, test, simulator, analysis |
| `mcp-figma` | Trích xuất Figma và handoff thiết kế |

### 14 Workflow Agents

#### Project Documentation Workflow

| Agent | Output |
|---|---|
| `write-project-docs` | Điều phối toàn bộ flow 5 tài liệu dự án |
| `write-project-overview` | `Project_Overview.md` |
| `write-use-cases` | `Use_Cases.md` |
| `write-functional-requirements` | `Functional_Requirements.md` |
| `write-wireframes` | `Wireframes.md` |
| `write-ux-flows` | `UX_Flows.md` |
| `review-project-docs` | Review và kiểm tra tính nhất quán |

#### Feature Development Workflow

| Agent | Output |
|---|---|
| `write-spec` | `requirements.md` |
| `write-design` | `design.md` |
| `write-tasks` | `tasks.md` |
| `execute-tasks` | Triển khai SwiftUI + tests |
| `refine-spec` | Cập nhật spec hiện có |
| `quick-implement` | Triển khai trực tiếp cho phạm vi nhỏ |
| `research-prd` | PRD draft từ ngữ cảnh nghiên cứu |

### Shared Guides

- `COMPONENT_FORMAT.md`
- `PBT_GUIDE.md`
- `PARALLEL_EXECUTION_GUIDE.md`
- `SPEC_WORKFLOW_GUIDE.md`

<p align="right">(<a href="#readme-top">lên đầu trang</a>)</p>

## Bắt đầu nhanh

### Điều kiện tiên quyết

- Cài [uv](https://docs.astral.sh/uv/getting-started/installation/)

### Cài cho Claude Code

```bash
uvx --from git+https://github.com/nguyennamkkb/ios-spec-driven ios-spec-driven install --ide claude
```

### Cài cho OpenCode

```bash
uvx --from git+https://github.com/nguyennamkkb/ios-spec-driven ios-spec-driven install --ide opencode
```

### Cấu hình Figma Token (Framelink MCP)

Sau khi cài đặt, hãy thay `YOUR_FIGMA_TOKEN` bằng token cá nhân của bạn:

- Claude Code: `.mcp.json`
- OpenCode: `.opencode/opencode.json`

Cách tạo Figma token:

- Xem hướng dẫn chính thức: https://help.figma.com/hc/en-us/articles/8085703771159-Manage-personal-access-tokens
- Quyền cần có: **File content (read)** và **Dev resources (read)**

<p align="right">(<a href="#readme-top">lên đầu trang</a>)</p>

## Sản phẩm đầu ra

### Output của Full Documentation Mode

```text
[.claude|.opencode]/specs/[project-name]/
  Project_Overview.md
  Use_Cases.md
  Functional_Requirements.md
  Wireframes.md
  UX_Flows.md
```

### Output của Feature Delivery Mode

```text
[.claude|.opencode]/specs/[feature-name]/
  requirements.md
  design.md
  tasks.md
```

Trình tự giao hàng điển hình:

```text
Ý tưởng
  -> nghiên cứu thị trường và định vị
  -> bộ tài liệu mục tiêu
  -> lập kế hoạch feature
  -> triển khai
  -> xác minh
```

Trình tự cho từng feature:

```text
Ý tưởng
  -> requirements
  -> design
  -> tasks
  -> triển khai
  -> xác minh
```

<p align="right">(<a href="#readme-top">lên đầu trang</a>)</p>

## Roadmap

- [ ] Cải thiện automated tests cho installer và template transformations
- [ ] Bổ sung release channels (`stable` và `dev`)
- [ ] Mở rộng tài liệu onboarding đa ngôn ngữ
- [ ] Mở rộng validation cho full project-document workflows

Xem [open issues](https://github.com/nguyennamkkb/ios-spec-driven/issues) để theo dõi thảo luận.

<p align="right">(<a href="#readme-top">lên đầu trang</a>)</p>

## Liên hệ

Nguyen Nam - nguyennamkkb@gmail.com

Project Link: [https://github.com/nguyennamkkb/ios-spec-driven](https://github.com/nguyennamkkb/ios-spec-driven)

<p align="right">(<a href="#readme-top">lên đầu trang</a>)</p>

<!-- MARKDOWN LINKS -->
[contributors-shield]: https://img.shields.io/github/contributors/nguyennamkkb/ios-spec-driven.svg?style=for-the-badge
[contributors-url]: https://github.com/nguyennamkkb/ios-spec-driven/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/nguyennamkkb/ios-spec-driven.svg?style=for-the-badge
[forks-url]: https://github.com/nguyennamkkb/ios-spec-driven/network/members
[stars-shield]: https://img.shields.io/github/stars/nguyennamkkb/ios-spec-driven.svg?style=for-the-badge
[stars-url]: https://github.com/nguyennamkkb/ios-spec-driven/stargazers
[issues-shield]: https://img.shields.io/github/issues/nguyennamkkb/ios-spec-driven.svg?style=for-the-badge
[issues-url]: https://github.com/nguyennamkkb/ios-spec-driven/issues
