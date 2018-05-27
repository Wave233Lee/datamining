package com.dragon.data.controller;

import com.dragon.data.domain.SOFTags;
import com.dragon.data.service.SOFTagsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.text.DecimalFormat;
import java.util.List;

@RestController
@RequestMapping(value = "/sofTags")
public class SOFTagsController {

    @Autowired
    private SOFTagsService sofTagsService;

    /**
     * 查询所有列表
     * @return
     */
    @RequestMapping(value = "/getAll")
    public List<SOFTags> sofTagsList(){
        return sofTagsService.findAll();
    }

    /**
     * 统计所有技能热度
     * @return
     */
    @RequestMapping(value = "/countAll")
    public long countAllSkill(){
        return sofTagsService.countAllSkill();
    }

    /**
     * 通过排名ID获取技能热度占比
     * @param id
     * @return
     */
    @RequestMapping(value = "/findOneById")
    public double findOneById(Integer id){
        DecimalFormat df = new DecimalFormat("#.0000");

        return Double.parseDouble(df.format((float)sofTagsService.findOneById(id).getTagpoints()/(float)sofTagsService.countAllSkill()));
    }
}
