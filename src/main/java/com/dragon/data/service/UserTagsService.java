package com.dragon.data.service;

import com.dragon.data.domain.UserTags;
import com.dragon.data.exceptions.Exceptions;
import com.dragon.data.repository.UserTagsRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.text.DecimalFormat;
import java.util.Collection;
import java.util.List;

@Service
public class UserTagsService {

    @Autowired
    private UserTagsRepository userRepository;

    /**
     * 新增
     * @param user
     * @return
     */
    public UserTags save(UserTags user){

        //验证是否存在
        if(user == null || user.getId() != null){
            throw new Exceptions(100,"not exist");
        }
        return userRepository.save(user);
    }

    /**
     * 更新
     * @param user
     * @return
     */
    public UserTags update(UserTags user){

        //验证是否存在
        if(user == null || user.getId() != null){
            throw new Exceptions(100,"not exist");
        }
        return userRepository.save(user);
    }

    /**
     * 删除
     * @param id
     */
    public void delete(Integer id){

        //验证是否存在
        if(!userRepository.existsById(id)){
            throw new Exceptions(100,"not exist");
        }
        userRepository.deleteById(id);
    }

    /**
     * 批量删除
     * @param users
     */
    public void deleteInBatch(Collection<UserTags> users){
        userRepository.deleteInBatch(users);
    }

    /**
     * 查询所有
     * @return
     */
    public List<UserTags> findAll(){
        return userRepository.findAll();
    }
    public Integer countTags(String skill){
        return userRepository.countTags(skill);
    }

    /**
     * 通过Id获取一个用户
     * @param id
     * @return
     */
    public UserTags getUserTagsById(Integer id){
        return userRepository.getOne(id);
    }
    /**
     * 技能排名
     * @param skill
     * @param score
     * @return
     */
    public double rankByTags(String skill, Integer score){
        return userRepository.rankByTags(skill, score);
    }

    public String findOneByUid(Integer userid){
        return userRepository.findOneByUid(userid).getUsername();
    }

    DecimalFormat df = new DecimalFormat("#.00");

    public double pointByTags1(Integer userid){
        double s = userRepository.findOneByUid(userid).getScore1();
        double r = userRepository.findOneByUid(userid).getReputation();
        return Double.parseDouble(df.format((s * 10)/r  + r/1000));
    }
    public double pointByTags2(Integer userid){
        double s = userRepository.findOneByUid(userid).getScore2();
        double r = userRepository.findOneByUid(userid).getReputation();
        return Double.parseDouble(df.format((s * 10)/r  + r/1000));
    }
    public double pointByTags3(Integer userid){
        double s = userRepository.findOneByUid(userid).getScore3();
        double r = userRepository.findOneByUid(userid).getReputation();
        return Double.parseDouble(df.format((s * 10)/r  + r/1000));
    }
    public double pointByTags4(Integer userid){
        double s = userRepository.findOneByUid(userid).getScore4();
        double r = userRepository.findOneByUid(userid).getReputation();
        return Double.parseDouble(df.format((s * 10)/r  + r/1000));
    }
}
