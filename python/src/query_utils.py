from typing import Any

def with_deleted_filter(stmt: Any, model: Any, include_deleted: bool):
    if include_deleted:
        return stmt
    return stmt.where(model.deleted_at.is_(None))
