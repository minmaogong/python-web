

from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["商品管理"]
)

# 定义用户相关路由
@router.get("/")
def get_all_items():
    return {"message": "获取所有商品列表"}

@router.get("/{item_id}")
def get_item(item_id: int):
    return {"message": f"获取 ID 为 {item_id} 的商品信息"}