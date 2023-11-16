from fastapi import APIRouter

router = APIRouter(
    prefix='/add',
    tags = ['addition']
)

@router.post('/send_data')
def send_data():
    
    return{
        "got it testing"
    }