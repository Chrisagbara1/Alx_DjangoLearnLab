## Permissions and Groups Setup

### Custom Permissions (on Book model in bookshelf app)
- `can_view`: View book list/details
- `can_create`: Add new book
- `can_edit`: Edit existing book
- `can_delete`: Delete book

### Groups and Their Permissions
- **Viewers**: `can_view`
- **Editors**: `can_create`, `can_edit`
- **Admins**: All permissions

### Notes
- Enforced via `@permission_required` decorator in views.
- Use Django Admin to assign users to groups.