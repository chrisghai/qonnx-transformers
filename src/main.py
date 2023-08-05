if __name__ == "__main__":
    import uvicorn
    #from app import app
    uvicorn.run("app:app", port=5000, reload=True)
