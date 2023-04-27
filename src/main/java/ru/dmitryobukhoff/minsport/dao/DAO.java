package ru.dmitryobukhoff.minsport.dao;

import lombok.Getter;
import lombok.Setter;
import lombok.extern.slf4j.Slf4j;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.springframework.stereotype.Repository;
import ru.dmitryobukhoff.minsport.util.HibernateUtil;

import java.util.List;

@Slf4j
@Getter
@Setter
@Repository
public abstract class DAO<T> {
    protected Class<T> modelClass;

    private SessionFactory sessionFactory;
    private Session currentSession;
    private Transaction currentTransaction;

    public DAO() {
        this.sessionFactory = HibernateUtil.getSessionFactory();
    }
    public void setModelClass(Class<T> modelClass) {
        this.modelClass = modelClass;
    }

    public Session openCurrentSession() {
        currentSession = sessionFactory.openSession();
        return currentSession;
    }

    public Session openCurrentSessionWithTransaction() {
        currentSession = sessionFactory.openSession();
        currentTransaction = currentSession.beginTransaction();
        return currentSession;
    }

    public void closeCurrentSession() {
        currentSession.close();
    }

    public void closeCurrentSessionWithTransaction() {
        currentTransaction.commit();
        currentSession.close();
    }

    public void persist(T obj) {
        openCurrentSessionWithTransaction().save(obj);
        closeCurrentSessionWithTransaction();
    }

    public T findById(Integer id) {
        T obj = openCurrentSession().get(modelClass, id);
        closeCurrentSession();
        return obj;
    }

    @SuppressWarnings("unchecked")
    public List<T> findAll() {
        List<T> listObj = openCurrentSession().createQuery("from " + modelClass.getName()).list();
        closeCurrentSession();
        return listObj;
    }

    public final void update(T obj) {
        openCurrentSessionWithTransaction().update(obj);
        closeCurrentSessionWithTransaction();
    }

    public void delete(T obj) {
        openCurrentSessionWithTransaction().delete(obj);
        closeCurrentSessionWithTransaction();
    }

}