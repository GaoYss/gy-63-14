from fastapi import APIRouter, Query

from app.modules.members.models import Member, MemberCreate, MemberUpdate
from app.modules.members.service import create_member, list_members, update_member

router = APIRouter()


@router.get("", response_model=list[Member])
def get_members(
    keyword: str | None = Query(default=None),
    level_id: int | None = Query(default=None, gt=0),
) -> list[Member]:
    return list_members(keyword, level_id)


@router.post("", response_model=Member, status_code=201)
def post_member(payload: MemberCreate) -> Member:
    return create_member(payload)


@router.patch("/{member_id}", response_model=Member)
def patch_member(member_id: int, payload: MemberUpdate) -> Member:
    return update_member(member_id, payload)
