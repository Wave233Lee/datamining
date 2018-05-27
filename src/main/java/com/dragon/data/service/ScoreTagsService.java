package com.dragon.data.service;

import com.dragon.data.domain.ScoreTags;
import com.dragon.data.repository.ScoreTagsRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ScoreTagsService {

    @Autowired
    private ScoreTagsRepository scoreTagsRepository;

    public List<ScoreTags> findAll(){
        return scoreTagsRepository.findAll();
    }

}
