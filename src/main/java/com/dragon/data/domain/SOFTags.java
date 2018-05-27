package com.dragon.data.domain;

import javax.persistence.*;

@Entity
@Table(name = "stackoverflow_tags")
public class SOFTags {

    /**
     * 主键ID
     */
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    private Integer id;

    /**
     * 技能名称
     */
    @Column(name = "tag_name")
    private String tagname;

    /**
     * 技能热度
     */
    @Column(name = "tag_points")
    private Integer tagpoints;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getTagname() {
        return tagname;
    }

    public void setTagname(String tagname) {
        this.tagname = tagname;
    }

    public Integer getTagpoints() {
        return tagpoints;
    }

    public void setTagpoints(Integer tagpoints) {
        this.tagpoints = tagpoints;
    }

    @Override
    public String toString() {
        return "SOFTags{" +
                "id=" + id +
                ", tagname='" + tagname + '\'' +
                ", tagpoints=" + tagpoints +
                '}';
    }
}
