from fastapi import HTTPException

def abort(code):
    raise HTTPException(code)
