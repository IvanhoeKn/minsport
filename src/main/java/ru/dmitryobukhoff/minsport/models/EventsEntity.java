package ru.dmitryobukhoff.minsport.models;

import javax.persistence.Basic;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Table;
import java.sql.Date;

@Entity
@Table(name = "events", schema = "public", catalog = "SportsProgrammingFederation")
public class EventsEntity {
    @Basic
    @Column(name = "id_event")
    private Integer idEvent;
    @Basic
    @Column(name = "full_description")
    private String fullDescription;
    @Basic
    @Column(name = "short_description")
    private String shortDescription;
    @Basic
    @Column(name = "location")
    private String location;
    @Basic
    @Column(name = "data_start")
    private Date dataStart;
    @Basic
    @Column(name = "data_end")
    private Date dataEnd;
    @Basic
    @Column(name = "organizer")
    private Integer organizer;
    @Basic
    @Column(name = "header")
    private String header;

    public Integer getIdEvent() {
        return idEvent;
    }

    public void setIdEvent(Integer idEvent) {
        this.idEvent = idEvent;
    }

    public String getFullDescription() {
        return fullDescription;
    }

    public void setFullDescription(String fullDescription) {
        this.fullDescription = fullDescription;
    }

    public String getShortDescription() {
        return shortDescription;
    }

    public void setShortDescription(String shortDescription) {
        this.shortDescription = shortDescription;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public Date getDataStart() {
        return dataStart;
    }

    public void setDataStart(Date dataStart) {
        this.dataStart = dataStart;
    }

    public Date getDataEnd() {
        return dataEnd;
    }

    public void setDataEnd(Date dataEnd) {
        this.dataEnd = dataEnd;
    }

    public Integer getOrganizer() {
        return organizer;
    }

    public void setOrganizer(Integer organizer) {
        this.organizer = organizer;
    }

    public String getHeader() {
        return header;
    }

    public void setHeader(String header) {
        this.header = header;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        EventsEntity that = (EventsEntity) o;

        if (idEvent != null ? !idEvent.equals(that.idEvent) : that.idEvent != null) return false;
        if (fullDescription != null ? !fullDescription.equals(that.fullDescription) : that.fullDescription != null)
            return false;
        if (shortDescription != null ? !shortDescription.equals(that.shortDescription) : that.shortDescription != null)
            return false;
        if (location != null ? !location.equals(that.location) : that.location != null) return false;
        if (dataStart != null ? !dataStart.equals(that.dataStart) : that.dataStart != null) return false;
        if (dataEnd != null ? !dataEnd.equals(that.dataEnd) : that.dataEnd != null) return false;
        if (organizer != null ? !organizer.equals(that.organizer) : that.organizer != null) return false;
        if (header != null ? !header.equals(that.header) : that.header != null) return false;

        return true;
    }

    @Override
    public int hashCode() {
        int result = idEvent != null ? idEvent.hashCode() : 0;
        result = 31 * result + (fullDescription != null ? fullDescription.hashCode() : 0);
        result = 31 * result + (shortDescription != null ? shortDescription.hashCode() : 0);
        result = 31 * result + (location != null ? location.hashCode() : 0);
        result = 31 * result + (dataStart != null ? dataStart.hashCode() : 0);
        result = 31 * result + (dataEnd != null ? dataEnd.hashCode() : 0);
        result = 31 * result + (organizer != null ? organizer.hashCode() : 0);
        result = 31 * result + (header != null ? header.hashCode() : 0);
        return result;
    }
}
