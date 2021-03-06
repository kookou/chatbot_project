import React from 'react';
import PropTypes from 'prop-types';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Rating from '@material-ui/lab/Rating';
import { Link } from 'react-router-dom'


const useStyles = makeStyles((theme) => ({
    divroot: {
        flexGrow: 1,
        marginTop: theme.spacing(3),

    },
    root: {
        display: 'flex',
        width: 500,

    },
    details: {
        display: 'flex',
        flexDirection: 'column',

    },
    content: {
        padding: 16,
        '&:last-child': {
            paddingBottom: 0,
        },
    },
    cover: {
        width: 150,
        height: 150,
    },

    paper: {
        padding: theme.spacing(2),
        textAlign: 'center',
        color: theme.palette.text.secondary,
    },
    none: {
        padding: 0
    },
    star: {
        marginBottom: 10
    },
    toolbarLink: {
        textDecoration: 'none',
    }

}));


const ShopList = (props) => {
    const classes = useStyles();
    const { post } = props;

    return (
        <div className={classes.divroot} spacing={2}>
            <Link to={"/shop/" + post.shop_id} className={classes.toolbarLink}>
                <Grid container justify="center"  >
                    <CardActionArea >
                        <Card className={classes.root} square elevation={0} variant="outlined">
                            <Grid item xs className={classes.details}>
                                <CardContent className={classes.content}>
                                    <Typography variant="h6">
                                        {post.shop_name}
                                    </Typography>

                                    <Grid container direction="row">
                                        <Rating name="iconstar" defaultValue={1} max={1} readOnly/>
                                        <Typography variant="subtitle1" color="textSecondary">
                                            {post.shop_rev_avg} /
                                            </Typography>
                                        <Rating name="iconstar" defaultValue={1} max={1} readOnly/>
                                        <Typography variant="subtitle1" color="textSecondary">
                                            예상 {post.shop_pred_avg}
                                        </Typography>
                                    </Grid>
                                    <Typography variant="subtitle1" color="textSecondary">
                                        리뷰  {post.shop_rev_cnt}
                                    </Typography>
                                    <Typography variant="subtitle1" color="textSecondary">
                                        대표메뉴 {post.food_name}
                                    </Typography>
                                </CardContent>
                            </Grid>
                            <CardMedia
                                className={classes.cover}
                                image={'https://www.yogiyo.co.kr' + post.shop_img}
                            />
                        </Card>
                    </CardActionArea>
                </Grid>
            </Link>
        </div >


    );
}

ShopList.propTypes = {
    post: PropTypes.object,
};

export default ShopList