package com.dragon.data.domain;

import javax.persistence.*;

@Entity
@Table(name = "user_tags")
public class UserTags {
    /**
     * 主键ID
     */
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Integer id;

    /**
     * 姓名
     */
    private String username;

    /**
     * 用户ID
     */
    private Integer userid;

    /**
     * 用户声望
     */
    private Integer reputation;

    /**
     * 标签1
     */
    private String tags1;

    /**
     * 分数1
     */
    private  Integer score1;

    /**
     * 标签2
     */
    private  String tags2;

    /**
     * 分数2
     */
    private  Integer score2;

    /**
     * 标签3
     */
    private  String tags3;

    /**
     * 分数3
     */
    private Integer score3;

    /**
     * 标签4
     */
    private String tags4;

    /**
     * 分数4
     */
    private Integer score4;


    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public Integer getUserid() {
        return userid;
    }

    public void setUserid(Integer userid) {
        this.userid = userid;
    }

    public Integer getReputation() {
        return reputation;
    }

    public void setReputation(Integer reputation) {
        this.reputation = reputation;
    }

    public String getTags1() {
        return tags1;
    }

    public void setTags1(String tags1) {
        this.tags1 = tags1;
    }

    public Integer getScore1() {
        return score1;
    }

    public void setScore1(Integer score1) {
        this.score1 = score1;
    }

    public String getTags2() {
        return tags2;
    }

    public void setTags2(String tags2) {
        this.tags2 = tags2;
    }

    public Integer getScore2() {
        return score2;
    }

    public void setScore2(Integer score2) {
        this.score2 = score2;
    }

    public String getTags3() {
        return tags3;
    }

    public void setTags3(String tags3) {
        this.tags3 = tags3;
    }

    public Integer getScore3() {
        return score3;
    }

    public void setScore3(Integer score3) {
        this.score3 = score3;
    }

    public String getTags4() {
        return tags4;
    }

    public void setTags4(String tags4) {
        this.tags4 = tags4;
    }

    public Integer getScore4() {
        return score4;
    }

    public void setScore4(Integer score4) {
        this.score4 = score4;
    }
}