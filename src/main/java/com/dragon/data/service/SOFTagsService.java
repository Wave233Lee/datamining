package com.dragon.data.service;

import com.dragon.data.domain.SOFTags;
import com.dragon.data.repository.SOFTagsRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class SOFTagsService {

    @Autowired
    private SOFTagsRepository sofTagsRepository;

    /**
     * 查询所有技能排行
     * @return
     */
    public List<SOFTags> findAll(){
        return sofTagsRepository.findAll();
    }

    /**
     * 统计所有技能总热度
     * @return
     */
    public long countAllSkill(){
        return sofTagsRepository.countAllSkill();
    }

    public SOFTags findOneById(Integer id){
        return sofTagsRepository.findById(id).get();
    }
}
