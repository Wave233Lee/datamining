package com.dragon.data.exceptions;

public class Exceptions extends RuntimeException{

    private Integer code;

    public Exceptions(Integer code, String message){
        super(message);
        this.code = code;
    }

    public Integer getCode() {
        return code;
    }

    public void setCode(Integer code) {
        this.code = code;
    }
}
